
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
__________________________________________________________________


======== ПРОТОКОЛИРОВАНИЕ (Использование модуля logging)  ========
        
С помощью журнальных сообщений можно увидеть что происходит в цикле

#! python3
# factorialLog.py

import logging
# logging.disable(logging.CRITICAL) # Отключение отладки(преимущество перед print())

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')

def factorial(n):
    logging.debug('Начало factorial(%s%%)'% (n))
    total = 1
    for i in range(1, n + 1):        # Начинаем с единицы
        total *= i
        logging.debug('i = ' + str(i) +', total = ' + str(total))
    logging.debug('Конец factorial(%s%%)'% (n))
    return total

print(factorial(5))
logging.debug('Конец программы')

Вывод:
    
 2023-04-15 15:15:05,423 - DEBUG - Начало программы
 2023-04-15 15:15:05,435 - DEBUG - Начало factorial(5)
 2023-04-15 15:15:05,437 - DEBUG - i = 1, total = 1
 2023-04-15 15:15:05,440 - DEBUG - i = 2, total = 2
 2023-04-15 15:15:05,442 - DEBUG - i = 3, total = 6
 2023-04-15 15:15:05,444 - DEBUG - i = 4, total = 24
 2023-04-15 15:15:05,446 - DEBUG - i = 5, total = 120
 2023-04-15 15:15:05,449 - DEBUG - Конец factorial(5)
120
 2023-04-15 15:15:05,455 - DEBUG - Конец программы



======== Уровни протоколирования ======================================

Уровень    Функция              Описание
-----------------------------------------------------------------------
DEBUG      logging.debug()      Низкий уровень. Диагностика проблем

INFO       logging.info()       Запись информации об обычных событиях
                                
WARNING    loggigng.warning()   Индикация потенциально опасных ситуаций

ERROR      logging.error()      Запись информации об ошибке

CRITICAL   logging.critical()   Высокий уровень для фатальных ошибок

>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.debug('Отладочная информация.')
2023-04-15 16:14:57,856 - DEBUG - Отладочная информация.
>>> logging.info('Работает модуль logging.')
2023-04-15 16:16:17,716 - INFO - Работает модуль logging.
>>> logging.warning('Риск получения сообщения об ошибке.')
2023-04-15 16:17:29,892 - WARNING - Риск получения сообщения об ошибке.
>>> logging.error('Произошла ошибка.')
2023-04-15 16:17:59,247 - ERROR - Произошла ошибка.
>>> logging.critical('Программа не может выполнятся.')
2023-04-15 16:18:53,092 - CRITICAL - Программа не может выполнятся.


Если передать функции аргумент (ERROR) level=logging.ERROR
отображаться будут лишь сообщения категорий ERROR и CRITICAL

Если передать функции аргумент (DEBUG) level=logging.DEBUG
отображаться будут сообщения всех категорий.(низкий уровень)


======== Отключение протоколирования ========================================

>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
>>> logging.critical('Критическая ошибка!')
 2023-04-15 16:30:59,157 - CRITICAL - Критическая ошибка!
>>> logging.disable(logging.CRITICAL)        # <============ Отключение протоколирования
>>> logging.critical('Критическая ошибка!')
>>> logging.error('Ошибка!')
>>> logging.warning('Предупреждение об ошибке!')


======== Запись сообщений в журнал файла ====================================

>>> import logging
>>> logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, \
		    format='%(asctime)s - %(levelname)s - %(message)s')


