"""Page listing the possible groceries"""
from os import path
from flask import render_template
from groceries.app import engine, app
from groceries.util import local_path


@app.route("/groceries")
def grocerypage():
    return render_template("groceries.html", groceries=engine.grocery_list.to_list())
