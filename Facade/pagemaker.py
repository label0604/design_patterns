import traceback
from configparser import ConfigParser


class Database:
    @classmethod
    def get_properties(cls, dbname):
        filename = dbname + '.ini'
        cp = ConfigParser()
        try:
            cp.read(filename, encoding='utf-8')
        except FileNotFoundError:
            print('Warning: {filename} is not found.'.format(
                filename=filename))
        return cp['Mail']


class HTMLWriter:
    def __init__(self, writer):
        self.writer = writer

    def title(self, title):
        self.writer.write('<html>')
        self.writer.write('<head>')
        self.writer.write('<title>{title}</title>'.format(title=title))
        self.writer.write('</head>')
        self.writer.write('</html>')
        self.writer.write('<body>\n')
        self.writer.write('<h1>{title}</h1>\n'.format(title=title))

    def paragraph(self, msg):
        self.writer.write('<p>{msg}</p>\n'.format(msg=msg))

    def link(self, href, caption):
        self.paragraph(
            '<a href="{href}">{caption}</a>'.format(href=href, caption=caption))

    def mail_to(self, mailaddr, username):
        self.link('mailto:{addr}'.format(addr=mailaddr), username)

    def close(self):
        self.writer.write('</body>')
        self.writer.write('</html>\n')


class PageMaker:
    @classmethod
    def make_welcome_page(cls, mailaddr, filename):
        try:
            mail_cp = Database.get_properties('maildata')
            username = mail_cp[mailaddr]
            with open(filename, mode='w', encoding='utf-8') as f:
                writer = HTMLWriter(f)
                writer.title(
                    'Welcome to {username}\'s page!'.format(username=username))
                writer.paragraph(username + 'のページへようこそ。')
                writer.paragraph('メール待っていますね。')
                writer.mail_to(mailaddr, username)
                writer.close()
            print('{filename} is created for {addr} ({username})'.format(
                filename=filename, addr=mailaddr, username=username))
        except Exception:
            print(traceback.format_exc())
