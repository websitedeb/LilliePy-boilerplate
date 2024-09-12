from flask import render_template, request

from ..app import returnFavicon, returnTitle


def render(content, Layout, title=None):
  converted = Layout(content.render()).render()
  if title != None:
    return render_template("main.html",
                           content=converted,
                           icon=returnFavicon(),
                           title=title)
  else:
    header = returnTitle()
    return render_template("main.html",
                           content=converted,
                           icon=returnFavicon(),
                           title=header)


def compare_dy_url(url):
  if url != "home":
    return request.path.startswith(url)
  else:
    return request.path == "/"
