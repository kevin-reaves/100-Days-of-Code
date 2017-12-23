"""
following Automate the Boring Stuff With Python


PDFs are binary. Can do things like add/delete/reorder
pages but can't really edit all the text or read
everything properly.
"""
import PyPDF2

#pdfObj = open("Kevin-Paladin.pdf", "rb")
#pdfRead = PyPDF2.PdfFileReader(pdfObj)

#print(pdfRead.numPages)

#page = pdfRead.getPage(0)
#print(page.extractText())

#for pageNum in range(pdfRead.numPages):
#    print(pdfRead.getPage(pageNum).extractText())

#Can combine PDF docs

paladinOpen = open("Kevin-Paladin.pdf", "rb")
wizardOpen = open("Kevin-Wizard.pdf", "rb")

paladin = PyPDF2.PdfFileReader(paladinOpen)
wizard = PyPDF2.PdfFileReader(wizardOpen)

writer = PyPDF2.PdfFileWriter()


for pageNum in range(paladin.numPages):
    page = paladin.getPage(pageNum)
    writer.addPage(page)
for pageNum in range(wizard.numPages):
    page = wizard.getPage(pageNum)
    writer.addPage(page)

palWiz = open("PalWiz.pdf", "wb")
writer.write(palWiz)
palWiz.close()

paladinOpen.close()
wizardOpen.close()