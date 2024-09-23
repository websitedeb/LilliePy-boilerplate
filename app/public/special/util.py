from flask import render_template, request

from ..app import returnFavicon, returnMeta, returnTitle


def render(content, Layout, title=None):
  converted = Layout(content.render()).render()
  if title != None:
    return render_template("main.html",
                           content=converted,
                           icon=returnFavicon(),
                           title=title,
                           meta=returnMeta())
  else:
    header = returnTitle()
    return render_template("main.html",
                           content=converted,
                           icon=returnFavicon(),
                           title=header,
                           meta=returnMeta())


def compare_dy_url(url):
  if url != "home":
    return request.path.startswith(url)
  else:
    return request.path == "/"
