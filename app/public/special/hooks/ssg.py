from markdown import markdown
from markdown_it import MarkdownIt


def use_ssg_file(loc):
  with open(f'../views/{loc}.md', "r") as md:
    if md.read() != "":
      mdx = MarkdownIt("commonmark", {'html': True, 'breaks': True})
      return mdx.render(md.read())
    else:
      return ""


def use_ssg_string(string):
  return markdown(string)
