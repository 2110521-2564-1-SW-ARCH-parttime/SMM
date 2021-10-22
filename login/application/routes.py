from os import name
from flask.helpers import url_for
from flask.wrappers import Response
from application import app,db
from flask import json, render_template, request, json, Response, flash, redirect
from application.models import User
from application.forms import LoginForm, RegisterForm

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",index=True)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        
        # print(user.password) # k9doaly

        if user and user.get_password(password):
            flash(f"{user.first_name}, You are successfully logged in!", "success")
            return render_template("index.html", login=True, name=user.first_name)
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        print(f"{user_id} {email} {password} {first_name} {last_name}")

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        flash("You are successfully registered!", "success")

        return render_template("index.html", login=True, name=user.first_name)

    return render_template("register.html", title="Register", form=form, register=True)


