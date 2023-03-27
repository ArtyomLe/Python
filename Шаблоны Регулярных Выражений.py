# (ШАБЛОН РЕГУЛЯРНОГО ВЫРАЖЕНИЯ) \d{3}-\d{3}-\d{4} == \d\d\d-\d\d\d\-\d\d\d\d
# r'...' == вызов необработаной строки (C:\Something\"BlaBla")
# re == Содержит различные функции для работы с регулярными выражениями
# Тестировщик регулярного выражения https://pythex.org/.

import re       # Модуль предназначенный для работы с регулярными выражениями

# Создание шаблона 
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')      # re.compile() cоздание обьекта Regex соответствующего шаблону тел. номера (Важно передавать необработаную r' ' строку поиского шаблона) 
# Поиск совпадений по заданному шаблону
mo = phoneNumRegex.search('My number: 415-444-4242.') # Метод .search() ищет в переданной ему строке любые совпадения с регулярными выражениями => (None/Match)
# Отображение найденных соответствий
print('Найденный номер телефона: ' + mo.group())      # Метод .group() возвращает найденные соответствия шаблону



=========================== Создание обьектов Regex ==============
import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number: 415-444-4242.')
print('Найденный номер телефона: ' + mo.group())




======================= Создание групп с помощью круглых скобок ==============
import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')  # (r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Мой номер: 415-555-4242.')
mo.group(1)     # '415'
mo.group(2)     # '555-4242'
mo.group(0)     # '415-555-4242'
mo.group()      # '415-555-4242'
mo.groups()     # ('415', '555-4242')

areaCode, mainNumber = mo.groups()
print(areaCode)     # 415
print(mainNumber)   # 555-4242

#Экранирование спец. символов .^$*+?{}[]\|() с помощью \(bla\) => \.\^\$\*\+\? и.т.д

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('Мой номер: (415) 555-4242.')
mo.group(1)     # (415)
mo.group(2)     # 555-4242



===================== Выбор альтернативных групп с помощью канала | ==============
Соответствие одному из нескольких альтернативных выражений (Символ канала |)


heroRegex = re.compile(r'Бэтмен|Тина Фей')
mo1 = heroRegex.search('Бэтмен и Тина Фей.')
mo1.group()     # Бэтмен

mo2 = heroRegex.search('Бетмен и Тина Фей.')
mo2.group()     # Тина Фей


                Схожий перфикс

batRegex = re.compile(r'Бэт(мен|мобиль|коптер|бэт)')
mo = batRegex.search('Бэтмобиль потерял колесо')
mo.group()      # Бэтмобиль
mo.group(1)     # мобиль




============ Указание необязательной группы с помощью (bla)? ====================


batRegex = re.compile(r'Бэт(ву)?мен')       # шаблон (ву)? не обязательная часть инструкции
mo1 = batRegex.search('Мой герой - Бэтмен')
mo1.group()     # Бетмен

mo2 = batRegex.search('Мой героиня - Бэтвумен')
mo2.group()     # Бетвумен


        Номера как содержащие код региона так и нет


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number: 415-555-4242')
mo1.group()     # 415-555-4242

mo2 = phoneRegex.search('My number: 555-4242')
mo2.group()     # 555-4242



============ Указание группы повторяющейся 0 или несколько раз с помощью * ====================
                      Найти нулевое или большее кол-во экземпляров


batRegex = re.compile(r'Бэт(ву)*мен') 
mo1 = batRegex.search('Мой герой - Бэтмен')
mo1.group()     # Бетмен

mo2 = batRegex.search('Мой героиня - Бэтвумен')
mo2.group()     # Бетвумен

mo3 = batRegex.search('Мой героиня - Бэтвувувувумен')
mo3.group()     # Бетвувувувумен



============ Указание группы повторяющейся 1 или несколько раз с помощью + ====================
                    Найти единичное или большее кол-во экземпляров


batRegex = re.compile(r'Бэт(ву)+мен') 
mo1 = batRegex.search('Мой героиня - Бэтвумен')
mo1.group()     # Бетвумен

mo2 = batRegex.search('Мой героиня - Бэтвувувувумен')
mo2.group()     # Бетвувувувумен

mo3 = batRegex.search('Мой герой - Бэтмен')
mo3 == None     # True




============ Указание кол-ва повторений с помощью фигурных скобок ====================


(Da){3}    => DaDaDa
(Da){3, 5} => диапазон повторений => DaDaDa или DaDaDaDa или DaDaDaDaDa
(Da){3, }  => 3 или более экземпляров группы Da
(Da){, 5}  => от 0 до 5 экземпляров группы Da


daRegex = re.compile(r'(Da){3}')
mo1 = daRegex.search('DaDaDa')
mo1.group()     # DaDaDa

mo2 = daRegex.search('Da')
mo2 == None     # True



============ Жадный нежадный виды поиска ==================================

>>> import re

>>> daRegex = re.compile(r'(Da){3,5}')
>>> mo1 = daRegex.search('DaDaDaDaDa')
>>> mo1.group()
'DaDaDaDaDa'

>>> daRegex = re.compile(r'(Da){3,5}?')
>>> mo2 = daRegex.search('DaDaDaDaDa')
>>> mo2.group()
'DaDaDa'

 ? - Может обозначать как нежадный поиск, так и необязательную группу.


============ Метод findall() ==========================================

.findall() - Возвращает строки каждого из найденных совпадений
.search()  - Возвращает первое найденное совпадение

>>> phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
>>> mo = phoneNumRegex.search('Mobile: 415-555-9999 Work: 212-555-0000')
>>> mo.group()
'415-555-9999'

# Нет групп
>>> phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
>>> phoneNumRegex.findall('Mobile: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

# Есть группы
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # (r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') == (r'\d{3}-\d{3}-\d{4}')
>>> phoneNumRegex.findall('Mobile: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]



============ Символьные классы =========================================

\d == (0|1|2|3|4|5|6|7|8|9)
\w == Любая буква цифра или символ подчёркивания
\s == Пробельные символы

[0-5] == (0|1|2|3|4|5)


>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 барабанщиков, 11 волынщиков, 10 лордов, 9 леди, 8 горничных, 7 лебедей, 6 гусей, 5 колец, 4 птицы, 3 курицы, 2 голубя, 1 куропатка')
['12 барабанщиков', '11 волынщиков', '10 лордов', '9 леди', '8 горничных', '7 лебедей', '6 гусей', '5 колец', '4 птицы', '3 курицы', '2 голубя', '1 куропатка']

\d+ == Текст содержащий одну или несколько цифр               ("+" один или больше)
\s  == За которыми следует пробел
\w+ == Текст содержащий букву, цифру или символ подчёркивания ("+" один или больше)

Метод findall() => Возвращает все совпавшие строки шаблона
регулярного выражения в виде списка



=========== Создание собственных символьных классов =========================================
Необходимость сопоставить регулярное выражение символам из определённого набора


>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']


Инверсия ^

>>> vowelRegex = re.compile(r'[^aeiouAEIOU]')
>>> vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

Диапазоны букв и цифр через дефис [a-zA-Z0-9]
Будет соответствовать всем буквам в нижнем и верхнем регистре а так же цифрам.


====================== Символы ^ $ =========================================
^ == Поиск соответствия в начале текста
$ == Поиск соответствия в конце текста

>>> import re
>>> beginsWithHello = re.compile(r'^Hello')
>>> mo = beginsWithHello.search('Hello, world!')
>>> mo.group()
'Hello'

>>> beginsWithHello.search('He said Hello') == None
True # Потому что не начинается с Hello



>>> endsWithNumber = re.compile(r'\d$') # Соответствие строки оканчивающиеся любой цифрой в диапазоне 0-9
>>> mo = endsWithNumber.search('Your number - 42')
>>> mo.group()
'2'

>>> endsWithNumber.search('Your number - forty two') == None
True # Потому что forty two не число



>>> wholeStringNum = re.compile(r'^\d+$') # Вся строка должна соостветствовать регулярному выражению 
>>> mo = wholeStringNum.search('1234567890')
>>> mo.group()
'1234567890'

>>> wholeStringNum.search('12345xyz67890') == None
True
>>> wholeStringNum.search('12 34567890') == None
True


============= Символ подстановки . (только для одного символа) =================================================

>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']    # 'lat' потому что только для одного символа



============= Поиск любого текста с помощью .* =========================================
















































