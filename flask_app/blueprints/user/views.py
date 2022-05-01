from flask import Blueprint, render_template

bp = Blueprint('user', __name__, template_folder="pages", url_prefix="/user")


@bp.route("/")
def home():
    return render_template("user/home.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    return render_template("user/register.html")