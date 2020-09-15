import mongoengine
class Coffee_machine(mongoengine.Document):
    Product_type=mongoengine.StringField(required=True)
    Water_line=mongoengine.BooleanField(required=True)
    Product_code=mongoengine.StringField(required=True)
    meta = {
        'db_alias':'core',
        'collection':'coffee_machine'
    }
