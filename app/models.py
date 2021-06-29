# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

from app import db, login_manager



origins = db.Table('origins',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('country_id', db.Integer, db.ForeignKey('countries.id'), primary_key=True)
)


class User(UserMixin, db.Model):
    """
    Create a users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger, unique=True)
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
    phone_number = db.Column(db.Integer, nullable=True)
    box_number = db.Column(db.Integer, nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    town = db.Column(db.String(20), nullable=True)
    county = db.Column(db.String(20), nullable=True)
    user_status = db.Column(db.Integer, db.ForeignKey('status.id'))
    household_no = db.Column(db.Integer, db.ForeignKey('households.id'), nullable=True)
    entitlement = db.Column(db.Integer, db.ForeignKey('entitlements.id'), nullable=True)
    id_no = db.Column(db.Integer, index=True, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    family_user = db.relationship('Family', backref='family_user', lazy='dynamic',)
 
    def __init__(self, user_id, box_number, password, postal_code, date_of_birth, email, username, county, country, town, id_no, phone_number, first_name, second_name, last_name):
        self.email = email
        self.username = username
        self.country = country
        self.town = town
        self.id_no = id_no
        self.phone_number = phone_number
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.county = county
        self.date_of_birth = date_of_birth
        self.postal_code = postal_code
        self.password = password
        self.box_number = box_number
        self.user_id = user_id


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


class Country(db.Model):
    """
    Create a countries table
    """

    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    m49_code = db.Column(db.Integer, unique=True)
    iso_alpha3 = db.Column(db.String(5), unique=True)
    country = db.relationship('User', backref='origin', lazy='select')
    

    def __init__(self, name, m49_code, iso_alpha3):
        self.name = name
        self.m49_code = code
        self.iso_alpha3 = iso_code

    def countries(self, name):
        return self.query.order_by(self.name).all()
       


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
    user_status = db.relationship('User', backref='status', lazy='dynamic')
    household_status = db.relationship('Household', backref='household_state', lazy='dynamic')

    def __repr__(self):
        return '<Status: {}>'.format(self.name) 

class Relation(db.Model):
    """
    Create a relation table
    """

    __tablename__ = 'relations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    relationship = db.relationship('Family', backref='relation', lazy='dynamic')
    

    def __repr__(self):
        return '<Relation: {}>'.format(self.name) 


class Family(db.Model):
    """
    Create a family table
    """

    __tablename__ = 'families'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    second_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    date_of_birth = db.Column(db.DateTime)
    relationship = db.Column(db.Integer, db.ForeignKey('relations.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__(self, id):
        self.id = id
        
        
    
    def __repr__(self):
        return '<Family: {}>'.format(self.family)


class Household(db.Model):
    """
    Create a household table
    """

    __tablename__ = 'households'

    id = db.Column(db.Integer, primary_key=True)
    household_no = db.Column(db.Integer, index=True, unique=True)
    household_create_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    household_update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    household_status = db.Column(db.Integer, db.ForeignKey('status.id'))
    household = db.relationship('User', backref='household', lazy='dynamic')
    

    def __init__(self, household_no):
        self.household_no = household_no
        

    def __repr__(self):
        return '<Household: {}>'.format(self.household) 


class Entitlement(db.Model):
    """
    Create an entitlements table
    """

    __tablename__ = 'entitlements'

    id = db.Column(db.Integer, primary_key=True)
    entitlement_no = db.Column(db.Integer)
    entitlement_create_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    entitlement_expiry_date = db.Column(db.DateTime, nullable=False)
    entitlement_status = db.Column(db.Boolean, default=False)
    entitlemant = db.relationship('User', backref='entitlement_id', lazy='dynamic')

    def __init__(self, entitlement_no, entitlement_expiry_date):
        self.entitlement_no = number
        self.entitlement_expiry_date = expiry

    def expiry(self, entitlement_create_date):
        self.entitlement_create_date = create_date

        

    def __repr__(self):
        return '<Entitlement: {}>'.format(self.entitlement) 
