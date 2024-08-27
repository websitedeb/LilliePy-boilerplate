from selenium import *
from flask import Flask
from reactpy import component


def render(comp):
  app = Flask(__name__)
  app.run(debug=True, port=1000)
