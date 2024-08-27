from markdown_it import MarkdownIt
from markdown import markdown


def use_ssg_file(loc):
  with open(f'../views/{loc}.md', "r") as markdown:
    if markdown.read() != "":
      md = MarkdownIt("commonmark", {'html': True, 'breaks': True})
      return md.render(markdown.read())
    else:
      return ""


def use_ssg_string(string):
  return markdown(string)
