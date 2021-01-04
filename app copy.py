from flask import Flask, request, render_template, jsonify, redirect, url_for, flash, send_file, send_from_directory, flash,session
from flask_migrate import Migrate
import time
import json
import requests
import os
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, IntegerField, FloatField, DateField, SelectField, SubmitField
from wtforms.validators import Required, InputRequired, DataRequired, Optional, Length, Email, URL, NumberRange, EqualTo, Regexp
app = Flask(__name__, static_folder='static')
app.config["SECRET_KEY"] = "hard to guess string"    # Important for CSRF token
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

class RegisterForm(FlaskForm):
    name = StringField("name", validators=[
                           InputRequired(), Length(min=1, max=20)])
    year = StringField("year", validators=[
                             InputRequired(), Length(min=1, max=4)])
    month = FloatField("month", validators=[
        Optional(),
        NumberRange(1, 12, "The month should be between %(min)s and %(max)s")])
    day = FloatField("day", validators=[
        Optional(),
        NumberRange(1, 31, "The day should be between %(min)s and %(max)s")])
    sex = StringField("sex", validators=[Optional(), URL()])
    # date = DateField("Start Date, ex: 2017/10/28", format='%Y/%m/%d')
    language = SelectField('Programming Language', choices=[(
        'cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def start():
    form = RegisterForm()
    formData = {
        'name': None,
        'year': None,
        'month': None,
        'day': None,
        'sex': None,
        'language': None
    }
    if form.validate_on_submit():
        formData = {
            'name': form.name.data,
            'year': form.year.data,
            'month': form.month.data,
            'day': form.day.data,
            'sex': form.sex.data,
            # 'date': form.date.data.strftime("%Y/%m/%d"),
            'language': form.language.data
        }
        session["formData"] = formData
        # return redirect(url_for("index"))
    elif form.errors and 'formData' in session:
        del session['formData']
    print(formData)
    return render_template("index.html", form=form, formData=session.get("formData"))


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static/image"), "favicon.ico", mimetype="image/favicon.ico")


if __name__ == '__main__':
    # #...中略...#
    # login = LoginManager(app)
    # login.login_view = 'login'
    app.debug = True
    # app.secret_key = "Your Key"
    # app.run(host= '0.0.0.0',port='4444')
    app.run(port='3333')
