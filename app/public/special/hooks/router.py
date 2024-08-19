from flask import request


def use_router(url):
  return url == request.path


def use_dynamic_router(base_url):
  path = request.path
  base_url = base_url.rstrip('/')
  path = path.rstrip('/')
  if path.startswith(base_url):
    return True
  return False
