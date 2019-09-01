from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users/SAGARI/Desktop/flaskapp/database.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username=uname, email=mail, password=passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


def init__db():
    db.create_all()


if __name__ == "__main__":
    init__db()
    app.run(debug=True)
