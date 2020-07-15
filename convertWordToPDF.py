import win32com.client, docx #install with "pip install pywin32" and "pip install python-docx"

wordFilename = 'example.docx'
pdfFilename = 'example.pdf'

doc = docx.Document()
doc.save(wordFilename)

wdFormatPDF = 17
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
