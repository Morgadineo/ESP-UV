# app/routes.py

from app import app
from flask import flash, redirect, render_template, url_for
from app.forms import LoginForm

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"""Login requested for user {form.username.data}, 
remember_me {form.remember_me.data}""")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)

@app.route("/")
@app.route("/home")
def home():
    """
    Página principal
    """
    return render_template("home.html", title="Home")




