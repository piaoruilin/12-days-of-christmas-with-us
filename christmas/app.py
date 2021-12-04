from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    password = request.form.get("password")
    if password != request.form.get("password-confirm"):
        return render_template("signup.html", error=True)
    
    return redirect("/")

@app.route("/day")
def day_one():
    return render_template("day.html")