# Участок импортируемых модулей.

from sys import argv

import urllib.request

from urllib.request import urlopen , Request

from html.parser import HTMLParser


# Участок классов.

'''class UrlRequest(Request):
    pass'''
    

# Класс парсера web-сайтов.
class WebParser(HTMLParser):

    # При инициализации объекта задаем параметры
    # для поиска информации с сайтов.
    def __init__(self):
        HTMLParser.__init__(self)
        self.__rHData = False
        self.__tags = ['meta']
        self.__nameDesc = ('name', 'description')
        self.__contDesc = 'content'
        self.__nameKey = ('name', 'Keywords')
        self.__contKey = 'content'
        self.__name = (self.__nameDesc, self.__nameKey)
        self.__cont = (self.__contDesc, self.__contKey)

    # Метод который принимает url сайта,
    # корректирует его(если надо) и декодирует в
    # читаемый вид. После чего, отдает
    # полученную страницу стандартному
    # методу feed на парсинг.
    def url_feed(self, url):
        try:
            #self.get('https://google.com')
            html = urlopen(url) 
            html = html.read().decode('UTF-8')
            self.feed(html)
        except ValueError:
            try:
                html = urlopen('https://' + url)
                html = html.read().decode('UTF-8')
                self.feed(html)
            except ValueError:
                try:
                    html = urlopen('http://' + url)
                    html = html.read().decode('UTF-8')
                    self.feed(html)
                except:
                    print('Попробуйте другой адрес.')
                    
    # Метод реагирует на стартовые тэги.
    #
    # Извлекает информацию из полученных атрибутов.
    def handle_starttag(self, tag, attrs):

        # Если теэ = титл, то меняет переменную.
        # Измененная переменная говорит методу
        # handle_data записать в переменную значение
        # текста, идущего после стартового тега титла.
        if tag == 'title':
            self.__rHData = True
            return

        # Если тэг такой, который мы ищем.
        # Если известные параметры совпадают
        # по значению.
        # То программа извлекает значение искомого
        # параметра, и печатает его в консоль.
        if tag in self.__tags:
            name = self.__name
            cont = self.__cont
            for i in range(0, len(name)):
                if name[i] in attrs:
                    if cont[i] in attrs[1][0]:
                        print('{0}: {1}\n'.format(name[i][1], attrs[1][1]))
                        print(attrs)
                        return

    # Если__rHData == True, то метод
    # извлекает в переменную и печатает ее
    # в консоль.
    def handle_data(self, data):
        if self.__rHData == True:
            self.data = data
            print('Title:', self.data, '\n')
            self.__rHData = False


# Участок функций.

def main():
    try:
        param = argv
        p = WebParser()
        p.url_feed(param[1])
    except:
        say = input('Наберите адрес сайта, с которого хотите получить данные:')
        p.url_feed(say)


# Участок, где начинает исполняться код.

if __name__ == '__main__':
    main()

    

