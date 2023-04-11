#! python3
# Перемена формата дат - переименовывает файлы, имена которых включают даты формата (mm-dd-yyyy) => (dd-mm-yyyy)
# Примеры допустимого формата: spam4-4-1984.txt или 01-03-2014eggs.zip
 
# os.listdir()         - Создаёт список всех файлов содержащихся в текущем каталоге
# os.path.join()       - 
# os.path.abspath('.') - Абсолютный путь данной директории откуда была запущена программа
# shutil.move()        - Выполняет переименование найденных файлов

import shutil, os, re

# Создание регулярного выражения которому соответствуют имена файлов содержащие даты в формате (mm-dd-yyyy)
# Данному рег. выражению будут соответствовать так же и недопустимые даты как 0-15-2014
datePattern = re.compile(r"""^(.*?)   # весь текст перед датой в имени файла
        ((0|1)?\d)-                   # одна или две цифры месяца (первой цифрой может быть как 0 так и 1)
                                      # (0|1)? => первая цифра месяца(0 или 1)  необязательна(?). Вторая цифра(\d) обязательная
        ((0|1|2|3)?\d)-               # одна или две цифры числа
                                      # (0|1|2|3)? => первая цифра дня необязательна(?). Вторая цифра(\d) обязательная  
        ((19|20)\d\d)                 # четыре цифры года
        (.*?)$                        # весь текст после даты в имени файла
        """, re.VERBOSE)

# Организация цикла по файлам в текущем каталоге
for amerFilename in os.listdir('.'):       # Просматриваем имена файлов из списка
    mo = datePattern.search(amerFilename)  # Сравниваем с нашим шаблоном

    # Пропуск файлов с именами не содержащими дат
    if mo == None:
        continue     # Если не найдено совпадения, то возвращаемся к счётчику for

    # Создаём переменные в случае совпадения с шаблоном
    # Для дальнейшего формирования имён файлов в европейском формате (dd-mm-yyyy)
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    
    '''Визуализация структуры групп в данном регулярном выражении (datePattern)

       datePattern = re.compile(r"""^(1) # beforePart(1)
        (2 (3) )-                        # monthPart(2)                                 
        (4 (5) )-                        # dayPart(4)                    
        (6 (7) )                         # yearPart(6) 
        (8)$                             # afterPart(8)
        """, re.VERBOSE)'''

    # Создание имен, соответствующих европейскому формату даты (конкатенируем строку)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Получение абсолютных путей к файлам
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Переименование файлов(Имена файлов выводятся на экран и переименовываются) 
    print(f'Заменяем "{amerFilename}" на "{euroFilename}" ...')
    #shutil.move(amerFilename, euroFilename) # Выполняет переименование найденных файлов



    
