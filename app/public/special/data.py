from flask import request, session


def get_cookie(cookie):
  return request.cookies.get(cookie)


def set_cookie(cookie, value):
  request.cookies.add(cookie, value)


def delete_cookie(cookie):
  del request.cookies[f"{cookie}"]


def check_cookie(cookie):
  return bool(get_cookie(cookie))


def get_session(ses):
  return session.get(ses)


def set_session(ses, value):
  session[ses] = value


def delete_session(ses):
  del session[ses]


def check_session(ses):
  return bool(get_session(ses))


def clear_sessions():
  session.clear()


def release_session(ses):
  session.pop(ses, None)
