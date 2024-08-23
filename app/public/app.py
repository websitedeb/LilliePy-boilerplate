from dominate import tags as html  # use this if you want to
from reactpy import component

from .special.hooks.router import use_dynamic_router
from .special.hooks.static import use_favicon, use_title

title, setTitle = use_title("Next.py Project")
favicon, setFavicon = use_favicon("favicon.ico")


@component
def App(var):
    if use_dynamic_router("/name"):
        return f"<h1> Hello {var.get('name')}! </h1>"
    else:
        if var:
            return f"<h1> {var} Next.py Project </h1>"
        else:
            return "<h1> Next.py Project </h1>"


def returnTitle():
    return title()


def returnFavicon():
    return favicon()
