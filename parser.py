# Участок импортируемых модулей.

from urllib.request import urlopen 

from html.parser import HTMLParser


# Участок классов.

class WebParser(HTMLParser):
    def __init__(self, url= ''):
        HTMLParser.__init__(self)
        self.__html = ''
        self.__textHtml = ''
        if url != '':
            self.urlOp(url)
    
    def urlOp(self, url):
        try:
            html = urlopen(url)
            self.initHtml(html)
        except ValueError:
            try:
                html = urlopen('https://' + url)
                self.initHtml(html)
            except ValueError:
                try:
                    html = urlopen('http://' + url)
                    self.initHtml(html)
                except ValueError:   
                    print('Вы не правильно ввели адрес сайта.')
        except ConnectionRefusedError:
            print('Такого адреса не существует, либо сайт исполльзует '+
                   'не протокол http(s)://. ' + 'Или сервер сайта не дает ' +
                  'подключиться.')                 

    def urlGet(self):
        geturl = self.__html.geturl()
        return geturl

    def prTxtHtml(self):
            text = self.__textHtml
            print(text)

    def byteInStr(self, html):
        text = html.read().decode('UTF-8')
        return text

    def initHtml(self, html):
        self.__html = html
        self.__textHtml = self.byteInStr(html)

    def html(self):
        return self.__html

    def textHtml(self):
        return self.__textHtml

    def handle_endtag(self, tag):
        if tag == 'title':
            print('Содержание тега title:', self.data)

    def handle_data(self, data):
        self.data = data



def main():
    parser = WebParser('google.com')
    print('parser creat')
    parser.urlOp('yandex.ru')
    print('вписали адрес урл')
    print(parser.urlGet())
    print('узнали урл в парсере')
    #print(parser.textHtml())
    print('Вывели текст html-страницы')
    parser.feed(parser.textHtml())
    
if __name__ == '__main__':
    main()
