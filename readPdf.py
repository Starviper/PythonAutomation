import PyPDF2


def getText(filename):
    pdf = PyPDF2.PdfFileReader(open(filename))
    fullText = []
    for pages in pdf.getNumPages():
        page = pdf.getPage(pages)
        fullText.append(page.extractText())
        pages = pages + 1
    return '\n'.join(fullText)