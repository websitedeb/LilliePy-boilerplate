from reactpy import component


@component
def Error(error, code=None):

  def isCode(e):
    if code:
      return f"\n <p>{e}</p> \n"
    else:
      return ""

  return f"""\n
  <div>
    <h1>Error: {error}</h1>
    {isCode(code)}
  </div>\n
  """
