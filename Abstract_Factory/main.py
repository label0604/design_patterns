import sys

from factory import Factory

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Usage: Python main.py factory.ListFactory or facotry.TableFactory')
        sys.exit()

    factory = Factory.get_factory(args[1])

    l_asahi = factory.create_link('朝日新聞', 'http://www.asahi.com/')
    l_yomiuri = factory.create_link('読売新聞', 'http://www.yomiuri.co.jp/')
    l_yahoo_us = factory.create_link('Yahoo!', 'http://www.yahoo.com/')
    l_yahoo_jp = factory.create_link('Yahoo!Japan!', 'http://www.yahoo.co.jp/')
    l_excite = factory.create_link('Excite', 'http://www.excite.com/')
    l_google = factory.create_link('Google', 'http://google.com/')

    t_news = factory.create_tray('新聞')
    t_news.add(l_asahi)
    t_news.add(l_yomiuri)

    t_yahoo = factory.create_tray('Yahoo!')
    t_yahoo.add(l_yahoo_us)
    t_yahoo.add(l_yahoo_jp)

    t_search = factory.create_tray('サーチエンジン')
    t_search.add(t_yahoo)
    t_search.add(l_excite)
    t_search.add(l_google)

    page = factory.create_page('LinkPage', '結城 浩')
    page.add(t_news)
    page.add(t_search)
    page.output()
