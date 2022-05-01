from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from .forms import UserForm

bp = Blueprint('user', __name__, template_folder="pages", url_prefix="/user")


@bp.route("/")
@login_required
def home():
    return render_template("user/home.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()
    return render_template("user/register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("user/login.html")


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    return redirect(url_for('landing_page.home'))
