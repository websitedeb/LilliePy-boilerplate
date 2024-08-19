from hooks.static import use_css, use_js
from reactpy import component


@component
def load():
  return f"""
    {use_js("pre_loader.dom")}
    {use_css("pre_loader")}
    <div class="preloader">loading...</div>
  """
