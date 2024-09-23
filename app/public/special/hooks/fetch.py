import requests as req


def use_fetch(url):
  return req.get(url).json()