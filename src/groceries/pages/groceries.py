"""Page listing the possible groceries"""
from flask import render_template, url_for, redirect, request
from groceries.app import engine, app


@app.route("/groceries")
def grocerypage():
    return render_template("groceries.html", groceries=engine.grocery_list.to_list())


@app.route("/add_groceries", methods=['POST'])
def add_groceries():
    engine.grocery_list.add_items_to_grocery_list(request.form.keys())
    return redirect(url_for("index"))

@app.route("/going_shopping")
def going_shopping():
    return render_template("going_shopping.html", shopping_list=engine.grocery_list.going_shopping())
    
@app.route("/done_shopping", methods=['POST'])
def done_shopping():
    engine.grocery_list.done_shopping(request.form.keys())
    # @todo: redirect to a page with an overview of the groceries bought today/still missing.
    return redirect(url_for("index"))