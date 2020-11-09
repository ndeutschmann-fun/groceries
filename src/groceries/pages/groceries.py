"""Page listing the possible groceries"""
from flask import render_template, url_for, redirect, request
from groceries.app import engine, app


@app.route("/groceries")
def grocerypage():
    return render_template("groceries.html", groceries=engine.grocery_list.to_list())


@app.route("/add_groceries", methods=['POST'])
def add_groceries():
    engine.grocery_list.add_items_to_grocery_list(request.form.keys())
    return redirect(url_for("grocerypage"))
