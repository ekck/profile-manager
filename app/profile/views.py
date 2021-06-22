# app/profile/views.py
from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from . import profile
from forms import DependantsForm, ContactsForm
from .. import db
from ..models import User

@profile.route('/registerdependant', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a user to the database through the registration form
    """
    form = DependantsForm()
    if form.validate_on_submit():
        dependant = Dependant(relationship=form.relationship.data,
                    first_name=form.first_name.data,
                    second_name=form.second_name.data,
                    last_name=form.last_name.data,
                    date_of_birth=form.date_of_birth.data)

        # add user to the database
        db.session.add(dependant)
        db.session.commit()
        flash('You have successfully registered a dependant!')

        # redirect to the login page
        return redirect(url_for('profile.register'))

    # load registration template
    return render_template('profile/register.html', form=form, title='RegisterDependant')

@profile.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    """
    Handle requests to the /register route
    Add a user to the database through the registration form
    """
    form = ContactsForm()
    if form.validate_on_submit():
        contact = Contact(phone_number=form.phone_number.data,
                    box_number=form.box_number.data,
                    postal_code=form.postal_code.data,
                    town=form.town.data,
                    country=form.country.data)
                    

        # add contact to the database
        db.session.add(contact)
        db.session.commit()
        flash('You have successfully add you contacts!')

        # redirect to the login page
        return redirect(url_for('profile.contact'))

    # load registration template
    return render_template('profile/contact.html', form=form, title='RegisterContacts')

@profile.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    
    
    return render_template('profile/user.html', user=user, title='MyProfile')


