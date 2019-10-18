from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("Home_Page.html")

@app.route("/Roblox")
def roblox():
    return render_template("Roblox.html")

@app.route("/Robux")
def robux():
    return render_template("Robux.html")

@app.route("/Earn")
def earn():
    return render_template("Free_Robux.html")

@app.route("/Profile")
def profile():
    return render_template("Profile.html")