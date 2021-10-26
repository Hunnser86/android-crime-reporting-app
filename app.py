import os
import json
from flask import (
    Flask, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
"""Makes an itteration of the app"""

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def go_home():
    """All the @app.routes in the code are used
       to map the specific URL to the associated function

    """
    return render_template("home.html")


@app.route("/get_reports")
def get_reports():
    """Here, the code extracts the reports from the database
       and exposes them to the front end

    """
    reports = mongo.db.reports.find()
    return render_template("reports.html", reports=reports)


@app.route("/add_report", methods=["GET", "POST"])
def add_report():
    """This function allows the user to add a report,
    by requesting the data from mongoDB and displaying
    it on the front end

    """
    crime_type = mongo.db.crime_type.find().sort("crime_type", 1)
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

    return render_template("add_report.html", crime_type=crime_type)


@app.route("/report_success")
def report_success():
    """A simple page to let the user know the report
       was added successfully

    """
    return render_template("report_success.html")


@app.route("/edit_success")
def edit_success():
    return render_template("edit_success.html")


@app.route("/edit_report/<report_id>", methods=["GET", "POST"])
def edit_report(report_id):
    if request.method == "POST":
        edit = {
            "report_name": request.form.get("report_name"),
            "crime_type": request.form.get("crime_type"),
            "android_name": request.form.get("android_name"),
            "occupation": request.form.get("occupation"),
            "crime_status": request.form.get("crime_status"),
            "report_description": request.form.get("report_description")

        }
        mongo.db.reports.update({"_id": ObjectId(report_id)}, edit)
        return redirect(url_for("edit_success"))

    report = mongo.db.reports.find_one_or_404({"_id": ObjectId(report_id)})
    return render_template("edit_report.html", report=report)


@app.route("/remove_success")
def remove_success():
    return render_template("remove_success.html")


@app.route("/remove_report/<report_id>")
def remove_report(report_id):
    """This function removes reports by targeting
    the ObjectId on the database

    """
    mongo.db.reports.remove({"_id": ObjectId(report_id)})
    return redirect(url_for("get_reports"))


@app.route("/known_androids")
def known_androids():
    data = mongo.db.known_androids.find()
    return render_template("known_androids.html", page="known_androids",
                           data=data, droids=[])


@app.route("/admin/load_known_androids")
def load_known_androids():
    """Here, the json data is preloaded
    from droids.json to improve speed.
    Then it checks the database to see if there are
    any multiple entries.  Only unique entries
    are displayed on the page

    """
    data = []
    with open("data/droids.json", "r") as json_data:
        data = json.load(json_data)
    for entry in data:
        if mongo.db.known_androids.count(entry) == 0:
            mongo.db.known_androids.insert_one(entry)
    return redirect(url_for("known_androids"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
