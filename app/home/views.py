# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

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
    Render the aboutpage template on the /about route
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

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")