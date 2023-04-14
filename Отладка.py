
============ Генерирование исключений =================================================

def boxPrint(symbol, width, height):
    # Исключения чтобы не вызвать ошибку в программе
    if len(symbol) != 1:
        raise Exception('Переменная symbol должна содержать один символ')
    if width <= 2:
        raise Exception('Значение width должно превышать 2.')
    if height <= 2:
        raise Exception('Значение height должно превышать 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Передаём аргументы функции через счётчик 
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ',3, 3)):

    try:
        boxPrint(sym, w, h)  # Пробуем передавать значения в функцию
    except Exception as err: # В случае возникновения ошибки сохраняем в переменной err
        print('Возникло исключение: ' + str(err))

Вывод:
    
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
Возникло исключение: Значение width должно превышать 2.
Возникло исключение: Переменная symbol должна содержать один символ


======== Сохранение обратной трассировки стека вызовов в виде строки ==============

>>> import traceback
>>> try:
	raise Exception('Это сообщение об ошибке.')
except:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('Стек вызовов записан в файл errorInfo.txt.')

114
Стек вызовов записан в файл errorInfo.txt
******************************************************
Число 114 - это значение, возвращаемое методом write()
которое равно количеству символов записанных в файл

traceback.format_exc() - функция для обработки исключений
и получение информации о стеке вызовов


======== Утверждения ===============================================================

assert - я утверждаю, что условие истинно, а если нет,
значит в программе есть ошибка поэтому её следует остановить.
В случае сбоя программа не должна обрабатывать инструкции
а должна аварийно завершить работу

>>> ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
>>> ages.sort()
>>> ages
[15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
>>> assert ages[0] <= ages[-1]
>>> ages.reverse()
>>> ages
[92, 80, 73, 57, 54, 47, 26, 22, 17, 15]
>>> assert ages[0] <= ages[-1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    assert ages[0] <= ages[-1]
AssertionError


======== Использование утверждений в программе имитирующей работу светофора ========

# Перекрёсток 4 улиц: Market, 2nd, Mission, 16th
# 'ns' - north/south
# 'ew' - east/west

market_2nd   = {'ns': 'green', 'ew': 'red'}  # Словарь ключ/значение
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():        # Перебирает ключи
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

#В любой момент времени по крайней мере один сигнал сфетофора красный
assert 'red' in stoplight.values(), 'Ни один из сигналов не является красным!' + str(stoplight)

switchLights(market_2nd)


Полученный результат при отладке:
    AssertionError: Ни один из сигналов не является красным!
        {'ns': 'yellow', 'ew': 'green'}


======== ПРОТОКОЛИРОВАНИЕ (Использование модуля logging)  ========
        











