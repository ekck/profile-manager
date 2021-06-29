# app/auth/forms.py

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, DateField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields import DateField, SelectFieldBase, FileField
from wtforms.fields.html5 import DateField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from ..models import User, Country



class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    country = StringField('Country')
    """
    country = QuerySelectField('Country of Origin',query_factory=countries, validators=[DataRequired()]) 
    """
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    box_number = IntegerField('P.O Box')
    postal_code = IntegerField('Postal Code')
    town = StringField('Town/City')
    county = StringField('County/Province')
    id_no = IntegerField('ID/Passport Number', validators=[DataRequired()])
    
    
    submit = SubmitField('Register')
    

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

    def validate_id(self, field):
        if User.query.filter_by(id_no=field.data).first():
            raise ValidationError('ID is already in use.')

    
        

    

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')