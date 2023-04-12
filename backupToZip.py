#! python3
# backupToZip.py - Копирует папку вместе со всем её содержимым в ZIP файл с инкрементируемым номером копии в имени файла

# os.path.abspath()  - Выдаёт абсолютный путь => C:\delicious
# os.path.basename() - Используется базовое имя папки C:\delicious => delicious
# os.path.exists()   - Проверка существования соответствующего файла
# os.walk()          - Перебор(listing) всех файлов и подпапок содерж. в данной папке
# os.path.join(foldername, filename))
# zipfile.ZipFile(имя, 'w') - Создание нового архива 'w'-write / Дополнение 'a'-add


import zipfile, os

def backupToZip(folder):             # folder Строка пути к папке
    # Создание резервной копии всего содержимого папки "folder" в виде ZIP файла
    folder = os.path.abspath(folder) # должен быть задан абсолютный путь => C:\delicious

    # Определяем, какое имя файла должна использовать функция, исходя из имён уже существующих файлов
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip' # "delicious_1.zip"
        if not os.path.exists(zipFilename):  # Как только обнаружен несуществующий файл
            break                            # Цикл завершается. Переходим к созданию ZIP-файла
        number = number + 1 # Если файл сущв. то добаляем 1 к названию(delicious_2.zip) и снова проверяем наличие такого файла 

    # Создание ZIP-файла
    print(f'Создание файла {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Перебираем всю структуру папки и сжимаем файлы содерж. в каждой подпапке
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Добавление файлов из папки {foldername}...')
        # Добавить в ZIP-архив текущую папку
        backupZip.write(foldername)

        # Добавить в ZIP-архив все файлы из данной папки
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue     # Не создавать резервные копии самих ZIP файлов
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\delicious')  # Передаём в функцию строку пути к папке(резервную копию которой нужно сделать)
