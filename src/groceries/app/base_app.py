"""Instantiation of the barebones Flask app"""
import os
from flask import Flask
import groceries

template_dir = os.path.join(os.path.dirname(groceries.__file__), "pages", "templates")
app = Flask(__name__, template_folder=template_dir)
app.config.update(EXPLAIN_TEMPLATE_LOADING=True)
