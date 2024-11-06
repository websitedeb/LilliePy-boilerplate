from flask import render_template, request

from ..app import returnFavicon, returnMeta, returnTitle


def compiler(element):
  data = element.render()
  tag = data["tagName"]
  children = data["children"]
  content = children[0] if len(children) > 0 else ""
  props = children[1] if len(children) > 1 else {}

  html_str = f"<{tag}"

  if props:
    for key, value in props.items():
      html_str += f' {key}="{value}"'

  html_str += f">{content}</{tag}>"

  return html_str


def render(content, Layout, title=None):
  converted = None
  try:
    converted = Layout(compiler(content)).render()
  except (TypeError):
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
