#! python3
# randomQuizGenerator.py - создаёт билеты с вопросами и ответами,
# расположенными в случайном порядке, вместе с ключами ответов в словаре
# Всего 50 штатов

import random
# Данные билетов: ключи(keys) - названия штатов(states)
#                 значения(values) - столицы(capitals)

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dacota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dacota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Генерируем 35 файлов билетов
for quizNum in range(35):

    # Создание файлов билетов и ключей ответов
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Запись заголовка билета
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')
    
    # Перемешивание порядка следования штатов
    states = list(capitals.keys())
    random.shuffle(states)

    # Организация цикла по всем 50 штатам и создания вопроса для каждого из них
    for questionNum in range(48):
        # Получение правильных и неправильных ответов
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())              # Дублируем значения из словаря capitals
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # Удаляем правильный ответ
        wrongAnswers = random.sample(wrongAnswers, 3)       # Выбираем 3 случайных значения
        answerOptions = wrongAnswers + [correctAnswer]      # [] - В каждом цикле правильный ответ будет разным
        random.shuffle(answerOptions)                       # Перемешиваем чтобы правильный ответ не всегда соостветствовал последнему варианту


    # Запись вариантов вопросов и ответов в файл билета
        quizFile.write(f"{questionNum + 1}. What is the Capital of {states[questionNum]}?\n\n")
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        # Запись ключа ответа в файл
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()





    
