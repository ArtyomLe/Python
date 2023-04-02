============ Обычный способ ===========================================

while True:
    print('Укажите ваш возраст:')
    age = input()
    try:
        age = int(age)
    except:
        print('Пожалуйста введите цифры.')
        continue                             # Возвращает в начало цикла
    if age < 1:
        print('Пожалуйста введите положительное число.')
        continue                             # Возвращает в начало цикла
    break                                    # Заканчивает цикл

print(f'Вам {age} лет.')


========= Модуль PyInputPlus ===========================================
(pip install --user pyinputplus) установка через командную строку windows
help(pyip.inputChoice)    Справка

import pyinputplus

inputStr()      - Передача польз. функции для проверки введённых данных
inputNum()      - Гарантирует ввод числа(int, float)
inputChoice()   - Выбор одного из предложенных вариантов
inputMenu()     - Отображает меню с числовыми или буквенными вариантами
inputDatetime() - Ввод значений даты и времени
inputYesNo()    - Ответ 'да\нет'
inputBool()     - Распознаёт ответ 'True/False'
inputEmail()    - Ввод адреса эл. почты
inputFilepath() - Ввод правильного имени файла и его наличие
inputPassword() - Отображает символы ***** вместо вводимых символов


>>> import pyinputplus as pyip
>>> response = pyip.inputNum()
five
'five' is not a number.            # Генерирует неправильный ответ вместо ошибки программы
42
>>> response
42
***********************************************************

>>> response = input('Введите число: ')
Введите число: 42
>>> response
'42'
>>> import pyinputplus as pyip
>>> response = pyip.inputInt(prompt='Введите число: ')  # Передаём строку приглашения с помощью аргумента prompt=
Введите число: кот
'кот' is not an integer.
Введите число: 42
>>> response
42

========= Аргументы min, max, greaterThan, lessThan ===================
Диапазон допустимых значений

>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Введите число: ', min=4)
Введите число: 3
Number must be at minimum 4.
Введите число: 4
>>> response
4

*******************************************************
>>> response = pyip.inputNum('Введите число: ', greaterThan=4)
Введите число: 4
Number must be greater than 4.
Введите число: 5
>>> response
5

*******************************************************

>>> response = pyip.inputNum('>', min=4, lessThan=6)
>6
Number must be less than 6.
>3
Number must be at minimum 4.
>4
>>> response
4

========= Аргумент blank ==============================================
Допуск ввода пустой строки

>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Введите число: ')
Введите число: 
Blank values are not allowed.
Введите число: 42
>>> response
42
>>> response = pyip.inputNum(blank=True)

>>> response
''


========= Аргументы limit, timeout, default ===========================
Заканчивать опрос после определённого количества попыток
или по истечении определённого кол-ва времени

>>> import pyinputplus as pyip
>>> response = pyip.inputNum('Enter number: ', limit=2)
Enter number: bla
'bla' is not a number.
Enter number: bla bla
'bla bla' is not a number.
<Завершение опроса>pyinputplus.RetryLimitException

>>> response = pyip.inputNum(timeout=10)
42 (Введено после 10 сек. ожидания)
<Завершение опроса>pyinputplus.TimeoutException

>>> response = pyip.inputNum(limit=2, default='N/A')
hello
'hello' is not a number.
shalom
'shalom' is not a number.
>>> response
'N/A'


========= Аргументы allowRegexes, blockRegexes ===========================
Указание допустимых значений с помощью регулярных выражений

Список разрешений:
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
XLII
>>> response
'XLII'
>>> response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
xlii
>>> response
'xlii'

**************************************************************************
Список блокировок:
>>> response = pyip.inputNum(blockRegexes = [r'[02468]$'])
42
This response is invalid.
44
This response is invalid.
43
>>> response
43

**************************************************************************
Совместное использование:
(Например: разрешаем ввод 'caterpillar', 'category' запрещаем другие строки содержащие 'cat'
 
>>> import pyinputplus as pyip
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'

========= Передача пользовательской функции проверки inputCustom() ==========
Последовательность цифр равная в сумме 10

>>> import pyinputplus as pyip
>>> def addsUpToTen(numbers):
	numbersList = list(numbers)
	for i, digit in enumerate(numbersList):
		numbersList[i] = int(digit)
	if sum(numbersList) != 10:
		raise Exception('Сумма долна быть 10, а не %s.' %(sum(numbersList)))
	return int(numbers)

>>> response = pyip.inputCustom(addsUpToTen)
123
Сумма долна быть 10, а не 6.
1235
Сумма долна быть 10, а не 11.
1234
>>> response
1234
>>> response = pyip.inputCustom(addsUpToTen)
hello
invalid literal for int() with base 10: 'h'
55
>>> response
55

========= Занять дурака =========================================================

import pyinputplus as pyip

while True:
    prompt = 'Хотите узнать, как занять дурака на несколько часов?'
    response = pyip.inputYesNo(prompt)
#   response = pyip.inputYesNo(prompt, yesVal = 'да', noVal='нет') #Поддержка других языков
#   if response == 'нет':
    if response == 'no':
        break
    
print('Спасибо! Желаю хорошего дня.')


========= Тест на умножение ====================================================

import pyinputplus as pyip
import time, random

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Выбираем два случайных числа для перемножения
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' %(questionNumber, num1, num2)

    try:
        # Правильные ответы задаются allowRegexes
        # Неправильные ответы задаются blockRegexes
        # В случае неправильного ответа отображается пользовательсткое сообщение
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)], \
                      blockRegexes=[('.*', 'Неправильно!')], \
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Время истекло!')
    except pyip.RetryLimitException:
        print('Кол-во попыток закончилось!')
    else:
        # Если в блоке try не возникло исключений
        print('Правильно!')
        correctAnswers += 1

    time.sleep(1)
print('Счёт: %s/%s'%(correctAnswers, numberOfQuestions))

































