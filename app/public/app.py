from dominate import tags as html  # use this if you want to
from reactpy import component

from .special.hooks.router import use_dynamic_router
from .special.hooks.static import use_favicon, use_title
from .special.layout import Layout

title, setTitle = use_title("LilliePy Project")
favicon, setFavicon = use_favicon("lillie.png")


@component
def App(var):
    if use_dynamic_router("/name"):
        return Layout(f"<h1> Hello {var.get('name')}! </h1>").render()
    else:
        if var:
            return Layout(f"<h1> {var} LilliePy Project </h1>").render()
        else:
            return Layout("<h1> LilliePy Project </h1>").render()


def returnTitle():
    return title()


def returnFavicon():
    return favicon()
