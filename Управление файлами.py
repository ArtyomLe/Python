======== Модуль shutil для работы с файлами =========================
shell utilities - утилиты командной оболочки
shutil.copy(источник, назначение)
shutil.copytree(источник, назначение)
shutil.move(источник, назначение)

# Папки и файлы должны существовать!

>>> import shutil, os
>>> from pathlib import Path
>>> p = Path.home()
>>> p
WindowsPath('C:/Users/ArtyomLe')
>>> shutil.copy(p / 'spam.txt', p / 'some_folder') 
'C:\\Users\\ArtyomLe\\some_folder\\spam.txt'       # Получаем путь к скопированому файлу

# Копии файла присваивается другое имя eggs2.txt
>>> shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
WindowsPath('C:/Users/ArtyomLe/some_folder/eggs2.txt') 

# Копируется папка со всем её содержимым
>>> shutil.copytree(p / 'spam', p / 'spam_backup')
WindowsPath('C:/Users/ArtyomLe/spam_backup')  

# Перемещаем файл в определённую папку(Если такой файл там существует то он будет заменён)
>>> shutil.move('C:\\Users\\ArtyomLe\\hello.txt', 'C:\\Users\\ArtyomLe\\spam')
'C:\\Users\\ArtyomLe\\spam\\hello.txt'

# Файл перемещается и переименовывается
>>> shutil.move('C:\\Users\\ArtyomLe\\hello.txt', 'C:\\Users\\ArtyomLe\\spam\\spam_hello.txt')
'C:\\Users\\ArtyomLe\\spam\\spam_hello.txt'


======== Безвозратное удаление файлов и папок ===========================

import os

os.unlink(путь) - удаляет файл по указанному пути
os.rmdir(путь) - удаляет папку по указанному пути(папка должна быть пустой)
shutil.rmtree(путь) - удаляет папку с её содержимым


======== Безопасное удаление с помощью модуля send2trash ================

pip install --user send2trash #Установка пакета через командную строку win

>>> import send2trash
>>> baconFile = open('becon.txt', 'a')    #Создаём файл
>>> baconFile.write('Becon not a veg.')
16
>>> baconFile.close()
>>> send2trash.send2trash('becon.txt')

# Функция только отправляет файлы в корзину но не восстонавливает их из неё


======== Обход дерева каталогов ==========================================

import os
os.walk(путь к папке) # Например ('C:\\Users')

На каждой итерации цикла возвращает 3 значения:
    1) Текущее имя папки (foldername)
    2) Имена подпапок содерж. в текущей папке (subfolders)
    3) Имена файлов содерж. в текущей папке (filenames)

C:\
|_delicious
  |_cats
  | |_catnames.txt
  | |_zophie.jpg
  |
  |_walnut
  | |_waffles
  |   |_butter.txt
  |
  |_spam.txt

import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('Текущая папка - ' + folderName)

    for subfolder in subfolders:
        print('ПОДПАПКА ПАПКИ ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('ФАЙЛ В ПАПКЕ ' + folderName + ': '+ filename)

    print('')


Текущая папка - C:\delicious
ПОДПАПКА ПАПКИ C:\delicious: cats
ПОДПАПКА ПАПКИ C:\delicious: walnut
ФАЙЛ В ПАПКЕ C:\delicious: spam.txt

Текущая папка - C:\delicious\cats
ФАЙЛ В ПАПКЕ C:\delicious\cats: catnames.txt
ФАЙЛ В ПАПКЕ C:\delicious\cats: zophie.jpg

Текущая папка - C:\delicious\walnut
ПОДПАПКА ПАПКИ C:\delicious\walnut: waffles

Текущая папка - C:\delicious\walnut\waffles
ФАЙЛ В ПАПКЕ C:\delicious\walnut\waffles: butter.txt


======== Сжатие и чтение zip файлов с помощью модуля zipfile ===============

 cats
 |_catnames.txt
 |_zophie.jpg
 spam.txt
  
  











