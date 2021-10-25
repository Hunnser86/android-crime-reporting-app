import os
import json
# from flask import (
#     Flask, render_template,
#     redirect, request, session, url_for)


def load_data():
    data = []
    with open("data/droids.json", "r") as json_data:
        data = json.load(json_data)
    for entry in data:
        if mongo.db.known_androids.count(entry) == 0:
            mongo.db.known_androids.insert_one(entry)