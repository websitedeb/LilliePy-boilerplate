from asyncio import sleep

import pyautogui as pag
from flask import Flask, render_template_string
from selenium import webdriver

global rendered, browserset, browser, driver
rendered = False
browserset = False
browser = None
driver = webdriver.Chrome


def renderer(comp, *params):
  template = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>testing server</title>
  </head>
  <body>
    {{ content|safe }}
  </body>
  </html>
  """

  app = Flask(__name__)

  @app.route('/')
  def index():
    if params != None:
      try:
        rendered = True
        return render_template_string(template, content=comp(params).render())
      except:
        rendered = False
        raise Exception("Somthing went wrong...")
    else:
      rendered = True
      return render_template_string(template, content=comp().render())

  app.run(host="0.0.0.0", port=3000)


def setBrowser(engine="chrome"):
  if rendered:
    browser = engine
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    if browser == "chrome":
      options = webdriver.ChromeOptions()
      options.add_argument("--headless=new")
      driver = webdriver.Chrome(options=options)
      browserset = True
    elif browser == "edge":
      options = webdriver.EdgeOptions()
      options.add_argument("--headless=new")
      driver = webdriver.Edge(options=options)
      browserset = True
    elif browser == "firefox":
      options = webdriver.FirefoxOptions()
      options.add_argument("--headless=new")
      driver = webdriver.Firefox(options=options)
      browserset = True
    elif browser == "safari":
      options = webdriver.SafariOptions()
      options.add_argument("--headless=new")
      driver = webdriver.Safari(options=options)
      browserset = True
    else:
      browserset = False
      raise Exception("Browser not supported")
  else:
    browserset = False
    raise Exception("You havent ran the render function!")


class Actions:

  def __inti__(self):
    if rendered and browserset:
      self.browser = browser
      self.driver = driver
    else:
      raise Exception(
          "Please set browser or run render function if you havnt done ither one."
      )

  def moveto(self, by, element):
    self.element = self.driver.find_element(by, element)

  def click(self):
    self.element.click()

  def type(self, text):
    self.element.send_keys(text)

  def press(self, key):
    self.element.send_keys(key)


class Screen:

  def __init__(self):
    if rendered and browserset:
      self.browser = browser
      self.driver = driver
    else:
      raise Exception(
          "Please set browser or run render function if you havnt done ither one."
      )

  def scroll(self, direction):
    if direction == "up":
      pag.scroll(-1)
    elif direction == "down":
      pag.scroll(1)
    elif direction == "left":
      pag.scroll(-1, -1)
    elif direction == "right":
      pag.scroll(1, 1)
    else:
      raise Exception("Direction not supported")

  async def wait(self, seconds):
    await sleep(seconds)


def end():
  quit()
