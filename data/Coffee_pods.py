import mongoengine

class Coffee_pod(mongoengine.Document):
    product_type=mongoengine.StringField(required=True)
    coffee_flavor=mongoengine.StringField(required=True)
    pack_size=mongoengine.IntField(required=True)
    product_code = mongoengine.StringField(required=True)
    meta = {
        'db_alias':'core',
        'collection':'coffee_pod'
    }
   