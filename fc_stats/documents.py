from elasticsearch_dsl import DocType
from elasticsearch_dsl.field import Text, Date, Ip, Boolean, Long


class PageHit(DocType):
    doc_id = Long()
    fc_user_id = Long()
    product_id = Long()

    permissions = Long(multi=True)
    access_time = Date()
    origin_ip = Ip()
    request_type = Text()
    uri = Text()
    page_number = Long()
    is_full = Boolean()
    is_known_article = Boolean()
    is_known_product = Boolean()

    class Meta:
        index = 'hits'

    def save(self, **kwargs):
        return super(PageHit, self).save(** kwargs)

    @classmethod
    def properties(cls):
        props = PageHit._doc_type.mapping.properties.to_dict()['doc']['properties'].keys()
        return [prop for prop in props]
