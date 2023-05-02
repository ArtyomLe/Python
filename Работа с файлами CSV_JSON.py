                        Работа с форматами CSV/JSON

============== Модуль CSV ==================================

Объект reader:
--------------

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
[['05.04.2015 13:34', ' Apples', ' 73'], ['05.04.2015 3:41', ' Cherry', ' 85'], ['06.04.2015 12:46', ' Pears', ' 14'], ['08.04.2015 8:59', ' Orange', ' 52'], ['10.04.2015 2:07', ' Apples', ' 152']]

exampleData[0][0]
'05.04.2015 13:34'
exampleData[0][1]
' Apples'
exampleData[0][2]
' 73'
exampleData[1][1]
' Cherry'
exampleData[4][1]
' Apples'



Чтение данных из обьекта reader в цикле for:
--------------------------------------------
# Для получения номера текущей строки используется переменная .line_num
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Строка #' + str(exampleReader.line_num) + ' ' + str(row))

    
Строка #1 ['05.04.2015 13:34', ' Apples', ' 73']
Строка #2 ['05.04.2015 3:41', ' Cherry', ' 85']
Строка #3 ['06.04.2015 12:46', ' Pears', ' 14']
Строка #4 ['08.04.2015 8:59', ' Orange', ' 52']
Строка #5 ['10.04.2015 2:07', ' Apples', ' 152']




Объект writer:
--------------

import csv
outputFile = open('output.csv', 'w', newline='') # 'w' - Открытие файла в режиме записи
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['steak', 'eggs', 'beer', 'lookas'])
24
outputWriter.writerow([1, 2, 3.141592, 4])
16

outputFile.close()



Аргументы delimiter/lineterminator:
-----------------------------------





