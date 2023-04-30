                       Работа с документами PDF и Word

================ PDF документы =======================================

pip install --user PyPDF2
 
>>> import PyPDF2
>>> pdfFileObj = open('meetingminutes.pdf', 'rb')
>>> pdfReader = PyPDF2.PdfReader(pdfFileObj)

>>> len(pdfReader.pages)
19
>>> pageObj = pdfReader.pages[0]

>>> pageObj.extract_text()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS  \n \nMeeting of March 7 ,
2014  \n \n \n \n  \n \n  \n \n   \nThe Board of Elementary and Secondary Education
shall provide leadership and \ncreate policies for education that
expand opportunities for children, empower \nfamilies and
communities, and advance Louisiana in an increasingly
\ncompetitive glob al market.  BOARD  \nof \nELEMENTARY  \nand  \nSECONDARY
\nEDUCATION  \n '

>>> pdfFileObj.close()



Дешифровка PDF-документов:
--------------------------
>>> import PyPDF2
>>> pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
>>> pdfReader.is_encrypted
True
>>> pdfReader.decrypt('rosebud')
<PasswordType.OWNER_PASSWORD: 2>
>>> pageObj = pdfReader.pages[0]
>>> pageObj.extract_text()



Создание PDF-документов:
------------------------
Копирование страниц

import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfReader(pdf1File)
pdf2Reader = PyPDF2.PdfReader(pdf2File)

pdfWriter = PyPDF2.PdfWriter()

for pageNum in range(len(pdf1Reader.pages)):
    pageObj = pdf1Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)

for pageNum in range(len(pdf2Reader.pages)):
    pageObj = pdf2Reader.pages[pageNum]
    pdfWriter.add_page(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()    



Поворот страниц:
----------------
import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]
page.rotate(90)
--Опущено--

pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()



Наложение страниц:
------------------
import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
minutesFirstPage = pdfReader.pages[0]

pdfWatermarkReader = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))

minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])

pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(minutesFirstPage)

for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

minutesFile.close()
resultPdfFile.close()



Шифрование PDF документов:
--------------------------

import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()
for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.pages[pageNum])

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)

resultPdf.close()




====== Проект: обьединение выбранных страниц из многих PDF документов =======================================

#! python3
# combinePdfs.py - обьединяет все PDF-файлы, находящиеся в текущем каталоге в единый PDF-документ

import PyPDF2, os

# Получение списка всех PDF-файлов и сортировка
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)      # Сортировка в алфавитном порядке

pdfWriter = PyPDF2.PdfWriter()    # Создаём объект для хранения объединённых PDF-файлов

# Организация цикла по всем PDF-файлам
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # Организация цикла по всем страницам за исключением первой, которые добавляются в результ. документ
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

# Сохранение результирующего PDF-документа в файле
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
print('Done')
pdfOutput.close()




========================= Документы Word ===========================================












