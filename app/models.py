# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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
    gender = db.Column(db.String(10), index=True)
    password_hash = db.Column(db.String(128))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    province_id = db.Column(db.Integer, db.ForeignKey('provinces.id'))
    is_admin = db.Column(db.Boolean, default=False)

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
    Create a Department table
    """

    __tablename__ = 'countries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    users = db.relationship('User', backref='country',
                                lazy='dynamic')

    def __repr__(self):
        return '<Country: {}>'.format(self.name)


class Province(db.Model):
    """
    Create a Province table
    """

    __tablename__ = 'provinces'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    countries = db.relationship('Country', backref='province',
                                lazy='dynamic')

    def __repr__(self):
        return '<Province: {}>'.format(self.name)

class Status(db.Model):
    """
    Create a status table
    """

    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('Users', backref='status',
                                lazy='dynamic')

    def __repr__(self):
        return '<Status: {}>'.format(self.name)

