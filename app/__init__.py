"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-chaaqcjhp8u791gvvk1g-a.oregon-postgres.render.com",
    database="todo_c2oe",
    user="root",
    password="qKoZyLhwQoHmbZR24DdPZVwHGPeE2IWf")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
