from reactpy import component

from .hooks.static import use_css, use_js


@component
def Load():
  return f"""
    {use_js("pre_loader.dom")}
    {use_css("pre_loader")}
    <div id="preloader">loading...</div>
  """
