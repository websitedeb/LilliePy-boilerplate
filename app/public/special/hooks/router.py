from flask import request, url_for


def use_router(url):
  return url == request.path


def use_dynamic_router(url, **values):
  dyurl = url_for(url, **values)
  return dyurl == request.path
