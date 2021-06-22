# app/auth/forms.py

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, DateField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields import DateField, SelectFieldBase, FileField
from wtforms.ext.sqlalchemy.fields import QuerySelectField



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
    country = QuerySelectField(label='Country of Origin',query_factory=lambda: User.query.order_by(User.first_name).all())
    date_of_birth = DateField(id='datepick')
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    marital_status = RadioField('Marital Status', choices=[('value','description'),('value_two','whatever')])
    identification = FileField(label='Upload ID photo',)
    
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