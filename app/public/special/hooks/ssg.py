from markdown_it import MarkdownIt


def use_ssg(loc):
  with open(f'../views/{loc}.md', "r") as markdown:
    md = MarkdownIt("commonmark", {'html': True, 'breaks': True})
    return md.render(markdown.read())
