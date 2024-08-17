from flask import request


def use_router(url):
  return url == request.path
