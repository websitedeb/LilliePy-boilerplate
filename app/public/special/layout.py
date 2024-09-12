from reactpy import component


@component
def Layout(children):
  return f"""
    <body>
      {children}
    </body>
  """
