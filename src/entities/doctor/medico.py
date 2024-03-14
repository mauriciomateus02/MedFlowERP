from flask_wtf import FlaskForm
from wtforms import StringField,validators

class doctor_validator(FlaskForm):
    crm = StringField('crm',validators=[validators.DataRequired()])
    name = StringField('name',validators=[validators.DataRequired()])
    phone = StringField('phone',validators=[validators.DataRequired()])
    birthDate = StringField('birthDate',validators=[validators.DataRequired()])