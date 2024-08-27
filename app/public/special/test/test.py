from flask import Flask, render_template_string, request
from selenium import webdriver


def renderer(comp):
  pass


class Actions:
  pass


class Screen:
  pass


'''
  PROCESS:
  1) first will take component into renderer
  2) then will host said component in a different port with a template_string,
  meaning requires a different flask server
  3) if error then it returns a error
  4) actions will be able to interact with the component (buttons, inputs)
  5)  screen will get or could set anything on the screen (id, class)
'''
