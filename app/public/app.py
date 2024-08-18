from reactpy import component

from .special.hooks.static import use_favicon, use_title

title, setTitle = use_title("Next.py Project")
favicon, setFavicon = use_favicon("favicon.ico")


@component
def App():
    return "<h1>test</h1>"


def returnTitle():
    return title()


def returnFavicon():
    return favicon()
