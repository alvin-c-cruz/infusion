from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash

from flask_app import db
from .forms import UserForm
from .models import User


bp = Blueprint('user', __name__, template_folder="pages", url_prefix="/user")


@bp.route("/")
@login_required
def home():
    return render_template("user/home.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if User.query.filter_by(email=email).first():
            flash(message="Email already registered.", category="error")
        elif password != confirm_password:
            flash(message="Password does not match.", category="error")
        else:
            user = User(
                email=email,
                name=name,
                password=generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=16)
            )
            db.session.add(user)
            db.session.commit()
            flash(message="Registration successful. Please confirming your email.", category="success")

            return redirect(url_for('landing_page.home'))
    return render_template("user/register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("user/login.html")


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    return redirect(url_for('landing_page.home'))
