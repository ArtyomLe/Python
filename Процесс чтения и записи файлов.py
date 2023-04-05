from pathlib import Path

**Режим открытия файлов open() 
>>> helloFile = open(Path.home() / 'hello.txt')
Или (В данном случае это одна и таже директория)
>>> helloFile = open('C:\\Users\\ArtyomLe\\hello.txt')

*Режим чтения содержимого файлов read()
>>> helloContent = helloFile.read()
>>> helloContent
'Hello, world!'         # То что было написано в файле hello.txt

*Альтернативный вариант readlines() получаем список строк
>>> sonnetFile = open(Path.home() / 'sonnet29.txt')
>>> sonnetFile.readlines()
["When, in disgrace with fortune and men's eyes,\n",
 'I all alone beweep my outcast state,\n',
 'And trouble deaf heaven with my bootless cries,\n',
 'And look upon myself and curse my fate,']              # То что было написано в файле sonnet29.txt

*Режим записи в файл open('blabla.txt', 'w')
                    .write('')
                    .close()
*Режим добавления    open('blabla.txt', 'a')

>>> baconFile = open('bacon.txt', 'w')        # Режим записи или затирания существующего
>>> baconFile.write('Hello, world!\n')
14
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a')        # Режим добавления к существующему
>>> baconFile.write('Bacon is not a veg.')
19
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello, world!
Bacon is not a veg.


=========== Сохранение переменных с помощью модуля shelve ===================

>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Софи', 'Питер', 'Саймон']
>>> shelfFile['Кошки'] = cats  # Ассоциируем список cats с ключом 'Кошки'
>>> shelfFile.close()


>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['Кошки']
['Софи', 'Питер', 'Саймон']
>>> shelfFile.close()


>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['Кошки']
>>> list(shelfFile.values())
[['Софи', 'Питер', 'Саймон']]
>>> shelfFile.close()


=========== Сохранение переменных с помощью функции pprint.pformat() =========

>>> import pprint
>>> cats = [{'name': 'Sofy', 'description': 'wide'},
	{'name': 'Piter', 'description': 'strong'}]
>>> pprint.pformat(cats)
"[{'description': 'wide', 'name': 'Sofy'},\n {'description': 'strong', 'name': 'Piter'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats= ' + pprint.pformat(cats) + '\n')
93
>>> fileObj.close()


>>> import myCats
>>> myCats.cats
[{'description': 'wide', 'name': 'Sofy'}, {'description': 'strong', 'name': 'Piter'}]
>>> myCats.cats[0]
{'description': 'wide', 'name': 'Sofy'}
>>> myCats.cats[0]['name']
'Sofy'







