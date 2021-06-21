# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create a users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    second_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    date_of_birth = db.Column(db.DateTime)
 
    

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Countries(db.Model):
    """
    Create a countries table
    """

    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    m49_code = db.Column(db.Integer, unique=True)
    iso_alpha3 = db.Column(db.String(5), unique=True)
    postal = db.relationship('Contacts', backref='country',
                                lazy='dynamic')


    def __repr__(self):
        return '<Country: {}>'.format(self.name)



class Status(db.Model):
    """
    Create a status table
    """

    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, default="Active")
    description = db.Column(db.String(200))
    

    def __repr__(self):
        return '<Status: {}>'.format(self.name) 

class Contacts(db.Model):
    """
    Create a contacts table
    """

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=False)
    box_number = db.Column(db.Integer(), nullable=False)
    postal_code = db.Column(db.Integer(), nullable=False)
    town = db.Column(db.String(20), nullable=False)
    county = db.Column(db.String(20), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    
    
    def __repr__(self):
        return '<Contact: {}>'.format(self.phone_number) 

class Dependants(db.Model):
    """
    Create a dependatnts table
    """

    __tablename__ = 'dependants'

    id = db.Column(db.Integer, primary_key=True)
    relationship = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(60), index=True)
    second_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    date_of_birth = db.Column(db.DateTime)
    
    
    
    def __repr__(self):
        return '<Dependant: {}>'.format(self.relationship)


