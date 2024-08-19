from reactpy import component

from .special.hooks.static import use_favicon, use_title

title, setTitle = use_title("Next.py Project")
favicon, setFavicon = use_favicon("favicon.ico")


@component
def App(var):
    return f"<h1> {var} Next.py Project </h1>"


def returnTitle():
    return title()


def returnFavicon():
    return favicon()
