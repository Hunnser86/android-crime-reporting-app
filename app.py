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


@app.route("/get_reports")
def get_reports():
    reports = mongo.db.reports.find()
    return render_template("reports.html", reports=reports)


@app.route("/add_report", methods=["GET", "POST"])
def add_report():
    if request.method == "POST":
        report = {
            "report_name": request.form.get("report_name"),
            "crime_type": request.form.get("crime_type"),
            "android_name": request.form.get("android_name"),
            "occupation": request.form.get("occupation"),
            "crime_status": request.form.get("crime_status"),
            "report_description": request.form.get("report_description")

        }
        mongo.db.reports.insert_one(report)
        return redirect(url_for("report_success"))
        
    return render_template("add_report.html")


@app.route("/report_success")
def report_success():
    return render_template("report_success.html")


@app.route("/edit_report/<report_id>", methods=["GET", "POST"])
def edit_report(report_id):
    report = mongo.db.reports.find_one({"_id": ObjectId(report_id)})
    return render_template("edit_report.html", report=report)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
