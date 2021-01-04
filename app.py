from flask import Flask, request, render_template, jsonify, redirect, url_for, flash, send_file, send_from_directory, flash, session
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

Name = ''
Sex = ''
Year = ''
Month = ''
Day = ''
birthday = ''


@app.route('/', methods=["GET", "POST"])
def start():
    error = None
    global Name, Sex, Year, Month, Day, birthday
    if request.method == 'POST':
        Name = request.form.get('name')
        Sex = request.form.get('sex')
        Year = request.form.get('year')
        Month = request.form.get('month')
        Day = request.form.get('day')
        birthday = str(Year)+'-'+str(Month)+'-'+str(Day)
        if (Sex == '男'):
            Sex = 'Man'
        else:
            Sex = 'Ms'
        # 檢查姓名有沒有含特殊字元
        string = "~!@#$%^&*()_+-*/<>,.[]\/"
        for i in string:
            if i in Name:
                error = "您的資料包含特殊字符"
        print(Name)
        print(Year)
        if (Name == '' or Year == ''):
            error = '資料填寫未完全'
        elif (error == None):
            print('Month'+Month)
            return redirect('/light')
    return render_template("index.html", error=error)  # 回傳登入畫面


@app.route('/light', methods=["GET", "POST"])
def light():
    global Name, Sex, Year, Month, Day, birthday
    print("123:"+Name)
    if request.method == 'POST':
        light_type = request.form['options']
        data = {"name": Name,
                "user_id": '123456789012345678901234567890123',
                "birthday": birthday,
                "sex": Sex,
                "light_type": light_type}
        r = requests.post(
            'https://asia-east2-guanyin-mother-300200.cloudfunctions.net/bright_lights', json=data)
        print(r.json())
    return render_template("light.html")  # 回傳登入畫面


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
