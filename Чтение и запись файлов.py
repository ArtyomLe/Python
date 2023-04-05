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
                                                                          
Получение абсолютного пути на основе относительного (на основе текущего каталога Path.cwd())

>>> from pathlib import Path
>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.cwd()/Path('my/relative/path')
WindowsPath('C:/Users/ArtyomLe/Downloads/Python-main/Python-main/my/relative/path')

Получение абсолютного пути на основе относительного (на основе домашнего каталога Path.hame())

>>> Path('my/relative/path')
WindowsPath('my/relative/path')
>>> Path.home()/Path('my/relative/path')
WindowsPath('C:/Users/ArtyomLe/my/relative/path')


Модуль os.path()

>>> import os
>>> os.path.abspath('.')
'C:\\Users\\ArtyomLe\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.path.abspath('.\Scripts')
'C:\\Users\\ArtyomLe\\AppData\\Local\\Programs\\Python\\Python39\\Scripts'

>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True

>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'


=========== Получение отдельных частей пути =====================================

>>> from pathlib import Path
>>> p = Path('C:/Users/ArtyomLe/spam.txt')
>>> p.anchor
'C:\\'
>>> p.parent
WindowsPath('C:/Users/ArtyomLe')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
'C:'

>>> from pathlib import Path
>>> import os
>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(calcFilePath)
'calc.exe'
>>> os.path.dirname(calcFilePath)
'C:\\Windows\\System32'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')
>>> calcFilePath.split(os.sep)
['C:', 'Windows', 'System32', 'calc.exe']
                                                                          
=========== Определение размеров файлов и содержимого папок =====================

>>> from pathlib import Path
>>> import os
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
27648        # Размер в байтах

>>> import os
>>> from pathlib import Path
>>> os.listdir('C:\\Windows\\System32')
# Возвращает список всех файлов в данной директории

Нахождение суммарного обьёма всех файлов находящихся в заданной папке

>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
	totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
>>> print(totalSize)
2059849637       # Размер в байтах

=========== Изменение списка файлов с помощью шаблонов =====================
>>> p = Path('C:/Users/ArtyomLe/Desktop')
>>> p.glob('*')
<generator object Path.glob at 0x000001786EC01F20>
>>> list(p.glob('*'))  '*' - Означает произвольное количество любых символов

Выведет все файлы заканчивающиеся на .txt
>>> p = Path('C:/Users/ArtyomLe/Desktop')
>>> p.glob('*.txt')
<generator object Path.glob at 0x000001786EBB6DD0>
>>> list(p.glob('*.txt')) 

Выведет любой одиночный символ(project1.docx, project9.docx да / project10.docx нет)
>>> list(p.glob('project?.docx'))


Выведет все файлы с любым трёхсимвольным расширением в котором средний символ x(txt, exe)
>>> list(p.glob('*.?x?'))

Обход списка
>>> p = Path('C:/Users/ArtyomLe/Desktop')
>>> for textFilePathObj in p.glob('*.txt'):
	print(textFilePathObj)
C:\Users\ArtyomLe\Desktop\IT Learning.txt
C:\Users\ArtyomLe\Desktop\Linux_soft.txt
C:\Users\ArtyomLe\Desktop\Octoeverywhere.txt
                                                                 
=========== Проверка существования пути ====================================

>>> winDir = Path('C:/Windows')
>>> notExistDir = Path('C:/This/Folder/Does/Not/Exist')
>>> calcFile = Path('C:/Windows/System32/calc.exe')
>>> winDir.exists()         #Проверяет если путь существует
True
>>> winDir.is_dir()         #Проверяет если путь сцществует и соответствует каталогу
True
>>> notExistDir.exists()
False
>>> calcFile.is_file()      #Если путь существует и соответствует файлу
True
>>> calcFile.is_dir()
False

Проверка наличия диска D:\
>>> dDrive = Path('D:/')
>>> dDrive.exists()
False
                                                                          













                                                                          
                                                                          















