def use_title(init):
  title = {"title": init}

  def setTitle(new):
    title["title"] = new

  def getTitle():
    return title["title"]

  return getTitle, setTitle


def use_favicon(path):
  icon = {
      "icon":
      f'''\n <link rel="icon" type="image/x-icon" href="../assets/{path}" /> \n'''
  }

  def setFavicon(new):
    icon[
        "icon"] = f'''\n <link rel="icon" type="image/x-icon" href="../assets/{new}" /> \n'''

  def getFavicon():
    return icon["icon"]

  return getFavicon, setFavicon


def use_css(file_path):
  return f"""\n <link href="../assets/{file_path}.css" rel="stylesheet" /> \n"""


def use_img(file_path, type):
  return f"""\n <img src="../assets/{file_path}.{type}" /> \n"""


def use_js(file_path):
  return f"""\n <script src="../assets/{file_path}.js"></script> \n"""


def use_fonts(path):
  return f"""\n <link href="../assets/{path}" rel="stylesheet" /> \n"""


def use_google_fonts(url):
  return f"""\n <link href="https://fonts.googleapis.com/css?family={url}" rel="stylesheet" /> \n"""


def use_icons(path):
  return f"""\n <link href="../assets/{path}" rel="icon" /> \n"""


def use_bootstrap_icons(classId):
  return f"""\n <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@{classId}/font/bootstrap-icons.css"> \n"""


def use_external_script(url):
  return f"""\n <script src="{url}"></script> \n"""
