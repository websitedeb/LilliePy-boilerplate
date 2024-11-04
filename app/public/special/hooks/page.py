def use_page(module, pkg):
  from importlib import import_module
  return import_module(f"...page.{module}", pkg)
