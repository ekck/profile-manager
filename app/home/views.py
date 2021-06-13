# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/about')
def aboutpage():
    """
    Render the about template on the /about route
    """
    return render_template('home/about.html', title="About")

@home.route('/contact')
def contactpage():
    """
    Render the homepage template on the /contact route
    """
    return render_template('home/contact.html', title="Contact")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")