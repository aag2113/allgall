import pytz
from datetime import datetime
from hashlib import md5

from django.core.management.base import BaseCommand

from elasticsearch.helpers import streaming_bulk
from elasticsearch_dsl import Index

from fc_stats.models import Product, Article, FcUser
from fc_stats.documents import PageHit
from fc_stats.connections import connections


class Command(BaseCommand):

    def import_hits(self, filepath):
        with open(filepath) as f:
            done = 0
            for _ in streaming_bulk(
                    connections.get_connection('default'),
                    (
                        self.line_to_page_hit(line).to_dict(include_meta=True) for line in f
                    )
            ):
                done += 1
                if done % 10000 == 0:
                    print("Done %d" % done)

    def line_to_page_hit(self, line):
        line_items = line.strip().split(',')
        access_time = line_items[0].strip()
        access_ip = line_items[1].strip()
        access_method = line_items[2].strip()
        access_user = line_items[3].strip()
        access_product = line_items[4].strip()
        access_permissions = line_items[5].strip()
        access_uri = line_items[6].strip()

        if not access_product or not access_user:
            return PageHit()

        if access_product == 'texis':
            return PageHit()

        time = datetime.strptime(access_time, "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.UTC)

        uri = access_uri.split("/")[-1]
        uri = uri.split(".")[0]
        uri = uri.split("-")

        is_full = None
        doc_id = uri[0]
        if "full" in doc_id:
            is_full = True
            doc_id = doc_id.replace("full", "")

        try:
            doc_id = int(doc_id)
        except:
            doc_id = None

        page_num = None
        if doc_id and len(uri) > 1:
            page_num = int(uri[-1])

        if doc_id:
            article, created = Article.objects.get_or_create(docid=doc_id)
        else:
            article, created = Article.objects.get_or_create(uri=uri)

        permissions = set()
        for permission in access_permissions.split(" "):
            permission = permission.replace("READ", "")
            permission = permission.lower()

            product, created = Product.objects.get_or_create(product_key=permission)
            permissions.add(product.pk)

        product, created = Product.objects.get_or_create(product_key=access_product)
        user, created = FcUser.objects.get_or_create(username=access_user)

        is_known_article = article.is_known
        is_known_product = product.is_real

        kwargs = {
            'doc_id': article.pk,
            'fc_user_id': user.pk,
            'product_id': product.id,
            'permissions': list(permissions),
            'access_time': time,
            'origin_ip': access_ip,
            'request_type': access_method,
            'uri': access_uri,
            'page_number': page_num,
            'is_full': is_full,
            'is_known_article': is_known_article,
            'is_known_product': is_known_product
        }
        hit_id = md5(line.encode('utf-8')).hexdigest()
        return PageHit(meta={'id': hit_id}, **kwargs)

    def handle(self, *args, **options):
        filepath = '~/Downloads/usage-201802.log'
        if Index('hits').exists():
            Index('hits').delete()
        PageHit.init()

        self.import_hits(filepath)
