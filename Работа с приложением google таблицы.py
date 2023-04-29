                    Работа с приложением google таблицы

=========================== Модуль EZSheets =============================
pip install --user ezsheets

import ezsheets

Пример идентификатора таблиц google sheets:
https://docs.google.com/spreadsheets/d/1KIQTTLq2gLPOrych9NN1BK1f58dYPo6YGdDQvrmX26E/edit#gid=0

>>>import ezsheets
>>>ss = ezsheets.Spreadsheet('1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E')
>>>ss
Spreadsheet(spreadsheetId='1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E')
>>>ss.title
'First spreadsheet'


Создание новой пустой таблицы:
------------------------------
>>>import ezsheets
>>>ss = ezsheets.createSpreadsheet('Название новой таблицы')
>>>ss.title
'Название новой таблицы'


Загрузка существующей таблицы в формате Excel в приложение google таблицы:
--------------------------------------------------------------------------
>>>import ezsheets
>>>ss = ezsheets.upload('example.xlsx')
>>>ss.title
'example'


Список таблиц в учётной записи:
-------------------------------
ezsheets.listSpreadsheets()
{'1FsMUeafB0mH_I2HOG_4hOVeOaGeo': 'example', '1UuhNhx-s7hAck_720FUg9GowUY': 'Название новой таблицы')



====================== Атрибуты объекта Spreadsheet ========================

import ezsheets
ss = ezsheets.Spreadsheet('1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E')
ss.title                              # Заголовок электронной таблицы
'First spreadsheet'
ss.title = 'Данные класса'            # Изменение заголовка
ss.spreadsheetId                      # Уникальный идентификатор (только для чтения)
'1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E'
ss.url                                # Исходная URL ссылка (только для чтения)
'https://docs.google.com/spreadsheets/d/1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E/'
ss.sheetTitles                        # Заголовки всех обьектов Sheet
('Sheet1', 'Sheet2', 'Sheet3')
ss.sheets                             # Обьекты sheet в этой таблице
(<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>, <Sheet sheetId=576255884, title='Sheet2', rowCount=1000, columnCount=26>, <Sheet sheetId=1841116945, title='Sheet3', rowCount=1000, columnCount=26>)
ss[0]                                 # Первый обьект Sheet в таблице
<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>
ss['Sheet1']                          # Доступ к листу по заголовку
<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>
del ss[1]                             # Удаление второго объекта Sheet из таблицы
ss.sheetTitles                        # Лист Sheet2 удалён
('Sheet1', 'Sheet3')
ss.refresh()                          # Обновление данных



Различные форматы загрузки:
---------------------------

import ezsheets
ss = ezsheets.Spreadsheet('1KIQTTLq2gLPOrych9NN1BK1f58dYPo6YGdDQvrmX26E')
ss.title
'Данные класса'

ss.downloadAsExcel()
'Данные_класса.xlsx'
ss.downloadAsCSV()       # Загружает только первый лист
'Данные_класса.csv'
ss.downloadAsHTML()
'Данные_класса.zip'
ss.downloadAsPDF()
'Данные_класса.pdf'
ss.downloadAsTSV()       # Загружает только первый лист
'Данные_класса.tsv'
ss.downloadAsODS()
'Данные_класса.ods'

ss.downloadAsExcel('a_different_filename.xlsx')
'a_different_filename.xlsx'



Удаление таблицы:
-----------------
import ezsheets
ss = ezsheets.createSpreadsheet('Delete me')  # Создание таблицы 
ezsheets.listSpreadsheets()                   # Проверка создания
{'14wULCoEGXriQRyuSyd72kq-24V-3vD0zEuI1ElxPdLI': 'Delete me'}
ss.delete('Delete me')                        # Удаление таблицы ss.delete(permanent=True) безвозратное удаление
ezsheets.listSpreadsheets()
{}


====================== Объекты Sheet ===================================

>>>import ezsheets
>>>ss = ezsheets.Spreadsheet('1KIQTTLq2gLPOrych9NN1BK8dYPo6YGdDQvrmX26E')

>>>ss.sheets
(<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>, <Sheet sheetId=1841116945, title='Sheet3', rowCount=1000, columnCount=26>)

>>>ss.sheets[0]             # Доступ к листам
<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>
>>>ss[0]
<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>

>>>ss.sheetTitles           # Заголовки всех обьектов Sheet
('Sheet1', 'Sheet3')

>>>ss['Sheet3']             # Доступ к листам возможен и по заголовку
<Sheet sheetId=1841116945, title='Sheet3', rowCount=1000, columnCount=26>
>>>ss['Sheet1']
<Sheet sheetId=0, title='Sheet1', rowCount=1000, columnCount=26>


Чтение и запись данных:
-----------------------

import ezsheets
ss = ezsheets.createSpreadsheet('Моя таблица')
sheet = ss[0]                  # Получить первый лист таблицы
sheet.title
'Sheet1'
sheet = ss[0]
sheet['A1'] = 'Имя'            # Установить значение в ячейке A1
sheet['B1'] = 'Возраст'
sheet['C1'] = 'Любимый фильм'
sheet['A1']                    # Чтение значения в ячейке A1
'Имя'
sheet['A2']                    # Пустые ячейки возвращают пустую строку
''
sheet[2, 1]                    # Столбец 2, строка 1 - тот же адрес что и B1
'Возраст'
sheet['B1']
'Возраст'
sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'Robocop'
sheet.refresh()



Адресация строк и столбцов (преобразования):
--------------------------------------------
Индексы столбцов и строк начинаются с 1

import ezsheets
ezsheets.convertAddress('A2')
(1, 2)
ezsheets.convertAddress(1, 2)
'A2'
ezsheets.getColumnLetterOf(2)
'B'
ezsheets.getColumnNumberOf('B')
2
ezsheets.getColumnLetterOf(999)
'ALK'
ezsheets.getColumnNumberOf('ZZZ')
18278

Адрес вида 'A2' - удобен для ввода в исходный код
Адрес вида кортежей (столбец, строка) - удобен для выполнения цикла с перебором диапазона адресов



Чтение и запись столбцов и строк целиком:
-----------------------------------------

import ezsheets
ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
sheet.getRow(1)                  # Первая строка - 1, а не 0
['НАИМЕНОВАНИЕ', 'ЦЕНА (за 1 кг)', 'ПРОДАНО (кг)', 'ВЫРУЧКА', '', '']
sheet.getRow(2)
['Картофель', '0.86', '21.6', '18.58', '', '']
columnOne = sheet.getColumn(1)

sheet.getColumn(1)              # Показываем данные из первого столбца
-Длинный список продуктов(опущено)-
sheet.getColumn('A')            # Показываем данные из первого столбца
-Длинный список продуктов(опущено)-

sheet.getRow(3)
['Бамия', '2.26', '38.6', '87.24', '', '']           # '' - пустые строки в таблице
sheet.updateRow(3, ['Тыква', '11.50', '20', '230'])  # Обновляем данные в строке
sheet.getRow(3)
['Тыква', '11.50', '20', '230', '', '']

columnOne = sheet.getColumn(1)

for i, value in enumerate(columnOne):
    # Создание списка Python со строками в верхнем регистре
    columnOne[i] = value.upper()
    
sheet.updateColumn(1, columnOne)    # Обновление всего столбца

***

rows = sheet.getRows()      # Получение всех строк таблицы
rows[0]                     # Проверка значений в первой строке
['НАИМЕНОВАНИЕ', 'ЦЕНА (за 1 кг)', 'ПРОДАНО (кг)', 'ВЫРУЧКА', '', '']
rows[1]
['КАРТОФЕЛЬ', '0.86', '21.6', '18.58', '', '']
rows[1][0] = 'ТЫКВА'        # Изменение названия продукта
rows[1]
['ТЫКВА', '0.86', '21.6', '18.58', '', '']
rows[10]
['БАМИЯ', '2.26', '40', '90.4', '', '']
rows[10][2] = '400'         # Изменение количества проданных товаров
rows[10][3] = '904'         # Изменение выручки
  
rows[10]
  
['БАМИЯ', '2.26', '400', '904', '', '']
sheet.updateRows(rows)      # Обновление электронной таблицы



*** Изменение размеров листа

>>>sheet.rowCount           # Кол-во строк на листе
23758
>>>sheet.columnCount        # Кол-во столбцов на листе
6
>>>sheet.columnCount = 4    # Изменить кол-во столбцов на 4
>>>sheet.columnCount
4



Создание и удаление листов:
---------------------------

