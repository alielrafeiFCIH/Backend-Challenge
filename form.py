from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField,MultipleFileField,TextAreaField

class machineform(FlaskForm):
    run = SubmitField('Run')
    product_type = StringField('Product Type')
    water_line = StringField('water_line')
class podform(FlaskForm):
    query=TextAreaField('query')
    run = SubmitField('Run')
    product_type = StringField('product_type')
    pack_size = StringField('pack_size')
    flavor = StringField('flavor')