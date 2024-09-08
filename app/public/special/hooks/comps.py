def use_component(module, pkg):
  from importlib import import_module
  return import_module(f"../comps/{module}", pkg)


def use_bootstrap_components():
  return "\n https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css \n"
