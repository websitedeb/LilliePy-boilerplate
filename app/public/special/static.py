def use_title(init):
  title = {"title": init}

  def setTitle(new):
    title["title"] = new

  def getTitle():
    return title["title"]

  return getTitle, setTitle


def use_css(file_path):
  return f"""\n <link href="../assets/{file_path}.css" rel="stylesheet" /> \n"""


def use_img(file_path, type):
  return f"""\n <img src="../assets/{file_path}.{type}" /> \n"""


def use_js(file_path):
  return f"""\n <script src="../assets/{file_path}.js"></script> \n"""
