from os import getenv

import flask
from dotenv import load_dotenv
from flask import request
from flask_cors import CORS
from public.app import App
from public.special.auth import login_user_auth, logout_user_auth, register_user
from public.special.data import *
from public.special.db import DB
from public.special.not_found import Not_Found
from public.special.socket import Socket
from public.special.store import Store
from public.special.util import compare_dy_url, render

server = flask.Flask(__name__,
                     static_folder="./public/assets",
                     template_folder="./public/views")

CORS(server)

#server.route("/your_url")


@server.route("/")
def index():
  return render(App(""))


@server.route("/<var>")
def dynamic(var):
  if compare_dy_url("/"):
    return render(App(var))
  else:
    return not_found(None)


@server.route("/name")
def vars():
  params = request.args.to_dict()
  return render(App(params))


@server.errorhandler(404)
def not_found(err):
  return render(Not_Found(), "404 ERROR"), 404


if __name__ == "__main__":
  server.run(host="0.0.0.0", port=8080)
