# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/budget")
def budget():
    data = {
        "date": "Jul 3, 07",
        "vamshi": 4300,
        "suresh": 5000,
        "total": 9300
    }
    return render_template("support.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
