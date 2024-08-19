from reactpy import component
from hooks.static import use_css, use_js


@component
def load():
  return f"""
    {use_js("pre_loader.dom")}
    {use_css("pre_loader")}
    <div class="preloader">loading...</div>
  """
