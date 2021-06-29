# app/profiles/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, DateField
from wtforms.validators import DataRequired, Email

from ..models import User


class DependantsForm(FlaskForm):
  
    relationship = StringField('Relationship', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField(id='datepick')
    submit = SubmitField('Register')

class ContactsForm(FlaskForm):

    phone_number = StringField('Phone Number', validators=[DataRequired()])
    box_number = StringField('P.O.Box', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    town = StringField('Town/City', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    country = StringField('County', validators=[DataRequired()])
    submit = SubmitField('Register')