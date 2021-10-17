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
        if request.form.get("email") == "test@technos.com":
            flash("You are successfully logged in!", "success")
            # return redirect("/index")
            return render_template("index.html", login=True)
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


