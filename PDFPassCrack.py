import PyPDF2
from pathlib import Path


dictionary = open('C:/Dictionary.txt')
theFile = Path('C:/PathtoFile.pdf')
for x in dictionary.readlines():
    var1 = PyPDF2.PdfFileReader.decrypt(theFile, dictionary.readline(x))
    if var1 == 0:
        x = x + 1
    else:
        print('The password is: ' + dictionary.readline(x))