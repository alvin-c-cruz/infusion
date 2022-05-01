from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    email = EmailField(label="Email", validators=[DataRequired(), Email()], render_kw={"autocomplete": "off"})
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Register", render_kw={"class_": "btn btn-success"})
