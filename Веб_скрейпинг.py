Веб Скрейпинг - термин, обозначающий использование программы для загрузки
и обработки содержимого веб-страниц

* webbrowser - Открытие браузера на определённой странице
* requests   - Загрузка файлов и веб-страниц из интернета
* Bs4        - Синтактический анализ HTML (парсинг)
* selenium   - Управление работой браузера (веб-формы, имитация щелчков мыши)


>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
True # Открывается веб-стрваница


================= mapIt.py =========================================================

#! python3
# mapIt.py - Открывает карту в браузере, используя почтовый адрес из командной строки или буфера обмена

# .join() - Метод join возвращает результат в виде одной строки
# webbrowser - Запуск браузера
# sys - Чтение аргументов командной строки
# sys.argv - Переменная в которой хранится список включающий имя программы и аргументы командной строки
# Если этот список включает что то кроме имени файла, то функция len(sys.argv) вернёт значение большее 1
# Указывая на то что в командной строке имеются дополнительные параметры

'''
Команда для запуска программы:
mapit 870 Valencia St, San Francisco, CA 94110
В этом случае переменная sys.argv будет содержать след. список:
['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco', ', ', 'CA', '94110']
Но в переменной address будет следующий список:
'870 Valencia St, San Francisco, CA 94110'  (из-за  среза [1:] mapIt.py не считаем)
'''

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # Получение почтового адреса из командной строки 
else:
    address = pyperclip.paste() # Получение почтового адреса из буфера обмена

webbrowser.open('https://www.google.com/maps/place/' + address)


================= Загрузка файлов requests =============================================

pip install requests (установка модуля)

# Response - Это обьект
# Атрибут  .status_code - Проверка успешности выполнения запроса
# Значение requests.codes.ok - Означает что запрос был успешно выполнен
# В случае успешного запроса страница сохраняется в виде строки в переменной text


>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code == requests.codes.ok # Проверяем была ли загрузка успешной
True
>>> len(res.text)
178978
>>> print(res.text[:250])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare



This eBook is for the use of anyone anywhere at no cost and with

almost no restrictions whatsoever.  You may copy it, give it away or

re-use it under the terms of the Projec


================= Проверка ошибок raise_for_status() =========================

Эффективный способ гарантировано остановить программу в случае неудачной загрузки

>>> import requests
>>> res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
>>> res.raise_for_status()
'''Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    res.raise_for_status()
  File "C:\Python39\lib\site-packages\requests\models.py", line 1021, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist
'''


Если неудачная загрузка не является препятствием для дальнейшего выполнения программы

>>> import requests
>>> res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
>>> try:
	res.raise_for_status()
except Exception as exc:
	print('Возникла проблема: %s' % (exc))

	
'''Возникла проблема: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist'''


================= Сохранение загруженных файлов на жёстком диске =================================

# Записываем веб страницу в файл в цикле for используя метод iter_content()

>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.raise_for_status()  # Проверяем была ли загрузка успешной
>>> playFile = open('RomeAndJuliet.txt', 'wb') # wb - write binar (for unicode)
>>> for chunk in res.iter_content(100000):     # Указываем размер фрагмента в байтах
	playFile.write(chunk)

	
100000
78978
>>> playFile.close()

Процесс загрузки и сохранения файла:

1) Вызов функции requests.get() для загрузки файла
2) Вызов функции open() с аргументом 'wb' для создания нового файла в режиме бинарной записи
3) Цикл по возвращаемому значению метода iter_content() обьекта Response
   Метод iter_content() на каждой итерации цикла возвращает фрагмент содержимого(порцию данных)
4) Вызов метода write() на каждой итерации для записи содержимого файла
5) Вызов метода close() для закрытия файла


================= HTML (парсинг разметки с помощью модуля bs4) =======================

pip install --user beautifulsoup4
pip install --user lxml
>>> import requests, bs4
>>> res = requests.get('https://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>


Загрузка HTML файла с жёсткого диска(файл должен находиться в том же каталоге откуда запущен пайтон)

>>> import bs4, lxml(как вариант парсера)
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser') # или 'lxml' парсер второго аргумента
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>



================= Поиск элемента с помощью метода select() ===============

Из обьекта BeautifulSoup, можно вызвать метод select() и передать ему строку CSS-селектора искомого элемента
CSS-селекторы как регулярные выражения только в HTML страницах

soup.select('div')
soup.select('#author') Элемент, атрибут id которого равен "author"
soup.select('.notice')
soup.select('div span')
soup.select('div>span')
soup.select('input[name]')
soup.select('input[type="button"]')


Извлечение элемента с идентификатором 'author' из файла example.html

>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
>>> elems = exampleSoup.select('#author')
>>> type(elems)                   # elems Список обьектов Tag
<class 'bs4.element.ResultSet'>
>>> len(elems)
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> str(elems[0])                 # Преобразование обьекта Tag в строку
'<span id="author">Al Sweigart</span>'
>>> elems[0].getText()            # Этот метод показывает содерж. текст 
'Al Sweigart'
>>> elems[0].attrs
{'id': 'author'}

Извлекаем все элементы <p>
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
>>> pElems[0].getText()
'Download my Python book from my website.'
>>> str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
>>> pElems[1].getText()
'Learn Python the easy way!'
>>> str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
>>> pElems[2].getText()
'By Al Sweigart'



================= Получение данных из атрибутов элемента .get() ==============================

Используем метод select() для нахождения элемнтов <span> и сохранения первого из них
в переменной spanElem. Передав методу get() имя атрибута 'id' получаем соотв. значение 'author'

>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
'<span id="author">Al Sweigart</span>'
>>> spanElem.get('id')           # Метод get() обьекта Tag
'author'
>>> spanElem.get('несуществующий_адрес')== None
True
>>> spanElem.attrs
{'id': 'author'}



================= Открытие всех результатов поиска searchpypi.py ========================

#! python3
# searchpypi.py - открывает несколько результатов поиска

import requests, sys, webbrowser, bs4
print('Поиск...') # Отображается при загрузке страницы результатов поиска
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Извлечение первых найденных ссылок
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Открытие отдельной вкладки для каждого результата
# После исследования через инструменты разработчика
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems)) # Меньшее из переданных ей чисел(кол-во ссылок)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Открытие ', urlToOpen)
    webbrowser.open(urlToOpen)

'''В результате открывается 5 вкладок браузера

C:\Users\ArtyomLe>searchpypi.py boring stuff
Поиск...
Открытие  https://pypi.org/project/boring/
Открытие  https://pypi.org/project/stuff/
Открытие  https://pypi.org/project/boring-logger/
Открытие  https://pypi.org/project/automateboringstuff2ndedition/
Открытие  https://pypi.org/project/automateboringstuff/
'''


================= Загрузка картинок из сайта xkcd.com (downloadXkcd.py) ========================


#! python3
# downloadXkcd.py - загружает все комиксы XKCD

import requests, os, bs4

url = 'https://xkcd.com'  # Начальный URL-адрес
os.makedirs('xkcd', exist_ok=True) # Сохраняем комикс в папке ./xkcd
                                   # exist_ok=True Предотвращает появление исключения в том случае если папка существует
while not url.endswith('#'):       # Последняя картинка на сайте заканчивается # 
    # Загрузка страницы
    print('Загружаемая страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Поиск URL-адреса изображения комикса
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        
        # Загрузить изображение
        print('Загружается изображение %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Сохранение изображения в папке ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Получение URL-адреса кнопки Prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Готово!')



================= Запуск браузера под управлением модуля Selenium ========================

pip install --user selenium

>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> type(browser)
<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
>>> browser.get('https://inventwithpython.com')


Методы обьекта WebDriver для поиска элементов
---------------------------------------------------------------------------------
Имя метода                                       |  Возвращаемый обьект WebElement
---------------------------------------------------------------------------------
browser.find_element_by_name(имя)                  Элементы содержащие атрибут
browser.find_elements_by_name(имя)                 с указанным именем
 
browser.find_element_by_class_name(имя)            Элементы использующие CSS класс
browser.find_elements_by_class_name(имя)           с указанным именем

browser.find_element_by_css_selector(селектор)     Элементы соответствующие указанному
browser.find_elements_by_css_selector(селектор)    селектору CSS

browser.find_element_by_id(id)                     Элементы с указанным идентификатором
browser.find_elements_by_id(id)

browser.find_element_by_link_text(текст)           Элементы <a> полностью совпадающие 
browser.find_elements_by_link_text(текст)          с указаным текстом

browser.find_element_by_partial_link_text(текст)   Элементы <a> содержащие указанный
browser.find_elements_by_partial_link_text(текст)  текст

browser.find_element_by_tag_name(имя)              Элементы с указанным именем тега
browser.find_elements_by_tag_name(имя)             без учёта регистра (<a> == 'a' & 'A')




Атрибуты и методы обьекта WebElement
---------------------------------------------------------------------------------
Атрибут или метод  |  Описание
---------------------------------------------------------------------------------
tag_name            Имя тега, например 'a' в случае элемента <a>
get_attribute(имя)  Значение атрибута с указанным именем для данного элемента 
text                Текст, содержащийся в элементе, например 'hello' в случае элемента <span>hello</span>
clear()             В случае текстового поля или текстовой области удаляет введённый тест
is_displayed()      Возвращает True если элемент видимый, в противном случае False
is_enabled()        Для элементов ввода возвращает True, если элемент активизирован, иначе False
is_selected()       Для флажков или переключателей воозвращает True, если элемент выбран.Иначе False
location            Словарь с ключами 'x' и 'y' для позиции элемента на веб-странице




from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Найден элемент <%s> с данным именем класса!' %(elem.tag_name))

except:
    print('Не удалось найти элемент с данным именем класса.')



================= Щелчок на веб-странице  =============================================


