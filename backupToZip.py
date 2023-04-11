#! python3
# backupToZip.py - Копирует папку вместе со всем её содержимым в ZIP файл с инкрементируемым номером копии в имени файла
# os.path.basename() - Используется базовое имя папки 
# os.path.exists()   - Проверка существования соответствующего файла
# os.walk()          - Перебор всех файлов и подпапок содерж. в данной папке

import zipfile, os

def backupToZip(folder):
    # Создание резервной копии всего содержимого папки "folder" в виде ZIP файла
    folder = os.path.abspath(folder) # должен быть задан абсолютный путь

    # Определяем, какое имя файла должна использовать функция, исходя из имён уже существующих файлов
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break      # Как только обнаружен несуществующий файл, цикл завершается. Это имя присвоится след. файлу
        number = number + 1

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
            if filename.startwith(newBase) and \
               filename.endswith('.zip'):
                continue  # Не создавать резервные копии самих ZIP файлов
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\delicious')
