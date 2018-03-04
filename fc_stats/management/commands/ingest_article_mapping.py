from django.core.management.base import BaseCommand

from fc_stats.models import Product, Article


class Command(BaseCommand):
    """
    Command to import known articles from the FactCite database.

    Need to perform this step so that we can:
    1. Differentiate known/real articles/products from those that are generated when ingesting log files
    2. Import article metadata (title, etc.) to make fc_stats views more readable
    """
    def update_article_mappings(self, filepath):
        with open(filepath) as f:
            header = f.readline()
            for count, line in enumerate(f):
                line_items = line.strip().split('\t')
                docid = int(line_items[0])
                article, created = Article.objects.get_or_create(docid=docid)
                product_1, created = Product.objects.get_or_create(product_key=line_items[2])
                if created:
                    product_1.is_real = True
                    product_1.save()
                product_2, created = Product.objects.get_or_create(product_key=line_items[3])
                if created:
                    product_2.is_real = True
                    product_2.save()

                article.title = line_items[1]
                article.products.add(product_1)
                article.products.add(product_2)
                article.is_known = True
                if len(line_items) > 4:
                    article.word_count = int(float(line_items[4]))
                article.save()

                if count % 1000 == 0:
                    print(count)


    def handle(self, *args, **options):
        filepath = '~/Downloads/raw_articles.csv'

        self.update_article_mappings(filepath)
