import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dataclasses import dataclass, field
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/go_home")
def go_home():
    return render_template("home.html")


@dataclass(frozen=True)
class Report:
    crime_type: str
    android_name: str
    unit_name: str
    occupation: str
    crime_status: str
    report_description: str


@app.route("/get_reports")
def get_reports():
    reports = mongo.db.reports.find()
    return render_template("reports.html", reports=reports)


@app.route("/add_report")
def add_report(Report):
    return render_template("add_report.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
