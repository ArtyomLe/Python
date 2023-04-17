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



================= Получение данных из атрибутов элемента ===============

















