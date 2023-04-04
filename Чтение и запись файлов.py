===================== Функция Path() ==========================================
Используется для корректной версии разделителя

>>> from pathlib import Path
>>> Path('spam', 'bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
>>> str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'

*************************************************************

>>> from pathlib import Path
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
	print(Path(r'C:\Users\ArtyomLe', filename))

	
C:\Users\ArtyomLe\accounts.txt
C:\Users\ArtyomLe\details.csv
C:\Users\ArtyomLe\invite.docx


=========== Использование оператора / для обьединения путей ===================

>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')

*************************************************************

>>> homeFolder = r'C:\Users\AI'
>>> subFolder = 'spam'
>>> homeFolder + '\\' + subFolder
'C:\\Users\\AI\\spam'
>>> '\\'.join([homeFolder, subFolder])
'C:\\Users\\AI\\spam'

*************************************************************
Для корректного обьединения путей независимо от операционной системы
используем модуль pathlib

>>> homeFolder = Path('C:/User/AI')
>>> subFolder = Path('spam')
>>> homeFolder / subFolder
WindowsPath('C:/User/AI/spam')
>>> str(homeFolder / subFolder)
'C:\\User\\AI\\spam'


=========== Текущий каталог (Current working directory - cwd) ============

>>> from pathlib import Path
>>> import os
>>> Path.cwd()
WindowsPath('C:/Python39')

Смена текущего каталога(при условии что он существует)

>>> os.chdir('C:\\Windows\\System32')
>>> Path.cwd()
WindowsPath('C:/Windows/System32')

Домашний каталог *************************

>>> Path.home()
WindowsPath('C:/Users/ArtyomLe')

Абсолютный и относительный путь **********

Абсолютный путь    - всегда начинается с имени корневой папки(C:\)
Относительный путь - указывается относительно текущего каталога программы(..\)
.  - текущая папка
.. - родительская


=========== Создание новых папок с помощью функции os.makedirs() ============

>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')

Создание каталога из обьекта Path(только один каталог за раз)

>>> from pathlib import Path
>>> Path(r'C:\delicious\walnut\waffles\spam').mkdir()

=========== Обработка абсолютных и относительных путей ======================

>>> Path.cwd()
WindowsPath('C:/Python39')
>>> Path.cwd().is_absolute()
True
>>> Path('delicious/walnut').is_absolute()
False                                                                          
                                                                          








