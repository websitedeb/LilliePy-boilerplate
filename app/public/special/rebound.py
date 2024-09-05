from time import sleep

from reactpy import component

from .error import Error
from .load import Load


@component
def Rebound(fallback):
  contents = fallback + Load().render()
  sleep(3)
  if ("<div id=\"preloader\">loading...</div>" in contents):
    return contents
  else:
    print(fallback)
    return Error("rebound error").render()
