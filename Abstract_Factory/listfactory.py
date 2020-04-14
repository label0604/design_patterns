import factory


class ListFactory(factory.Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)


class ListLink(factory.Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return '<li><a href="{url}">{caption}</a></li>\n'.format(url=self.url, caption=self.caption)


class ListTray(factory.Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buffer = []
        buffer.append('<li>\n')
        buffer.append('{caption}\n'.format(caption=self.caption))
        buffer.append('<ul>\n')
        for item in self.tray:
            buffer.append(item.make_html())
        buffer.append('</ul>\n')
        buffer.append('</li>\n')
        return "".join(buffer)


class ListPage(factory.Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        buffer = []
        buffer.append(
            '<html><head><title>{title}</title></head>\n'.format(title=self.title))
        buffer.append('<body>\n')
        buffer.append('<h1>{title}</h1>\n'.format(title=self.title))
        buffer.append('<ul>\n')
        for item in self.content:
            buffer.append(item.make_html())
        buffer.append('</ul>\n')
        buffer.append(
            '<hr><address>{author}</address>'.format(author=self.author))
        buffer.append('</body></html>\n')
        return ''.join(buffer)
