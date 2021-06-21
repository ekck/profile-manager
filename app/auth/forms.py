# app/auth/forms.py

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, DateField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields import DateField



from ..models import User


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
    country = StringField('Country of Origin', validators=[DataRequired()])
    date_of_birth = DateField(id='datepick')
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    marital_status = StringField('Marital Status', validators=[DataRequired()])
    identiication = StringField('Upload ID', validators=[DataRequired()])
    submit = SubmitField('Register')
    

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')