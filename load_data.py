import os
import json
from flask import (
    Flask, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


@app.route("/load_data", methods=["GET", "POST"])
def load_data():
    known_android = mongo.db.known_androids.find().sort
    return render_template("known_androids.html", known_android=known_android)