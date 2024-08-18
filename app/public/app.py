from reactpy import component

from .special.hooks.static import use_title

title, setTitle = use_title("Next.py Project")


@component
def App():
    return ""


def returnTitle():
    return title()
