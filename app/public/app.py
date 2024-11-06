from reactpy import component, html

from .special.hooks.router import use_dynamic_router
from .special.hooks.static import use_favicon, use_meta, use_title

title, setTitle = use_title("LilliePy Project")
favicon, setFavicon = use_favicon("lillie.png")


@component
def App(var):
    if use_dynamic_router("/name"):
        return html.h1(f"Hello {var.get('name')}!", {"id": "greeting"})
    else:
        if var:
            return html.h1(f"{var}'s Lilliepy Project", {"class": "greeting"})
        else:
            return html.h1("Lilliepy Project")


def returnTitle():
    return title()


def returnFavicon():
    return favicon()


def returnMeta():
    return use_meta({
        'description': 'LilliePy Project',
        'keywords': 'Lilliepy',
        'author': 'name'
    })
