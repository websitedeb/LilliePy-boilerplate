import flask
from flask import render_template, request
from flask_cors import CORS
from public.app import App, returnFavicon, returnTitle
from public.special.not_found import Not_Found

server = flask.Flask(__name__,
                     static_folder="./public/assets",
                     template_folder="./public/views")

CORS(server)


def render(content, icon, title=None):
  converted = content.render()
  if title != None:
    return render_template("main.html",
                           content=converted,
                           icon=icon,
                           title=title)
  else:
    header = returnTitle()
    return render_template("main.html",
                           content=converted,
                           icon=icon,
                           title=header)


def compare_dy_url(url):
  if url != "home":
    return request.path.startswith(url)
  else:
    return request.path == "/"


#server.route("/your_url")


@server.route("/")
def index():
  return render(App(""), icon=returnFavicon())


@server.route("/<var>")
def dynamic(var):
  if compare_dy_url("/"):
    return render(App(var), icon=returnFavicon())
  else:
    return not_found(None)


@server.errorhandler(404)
def not_found(err):
  return render(Not_Found(), returnFavicon(), "404 ERROR"), 404


if __name__ == "__main__":
  server.run(host="0.0.0.0", port=8080)
