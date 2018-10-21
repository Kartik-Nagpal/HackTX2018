# This takes in a PDF Document and then attempts to get all
# Date information out of it.


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

# TODO: PDF text sometimes can't read tables properly.

class PDFConverter:

    # text
    pdfText = ""

    # Given a link to a PDF location, convert it to a string.
    # Returns a string of all the text in a PDF Document
    # Max length string is as long mem will allows.
    def pdfToText(self, path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()
        return text

    # linkToPDF is a link to PDF
    def __init__(self, linkToPdf):

        # The text extracted from a pdf, with some formatting
        self.pdfText = self.pdfToText(linkToPdf)


    def getText(self):
        return self.pdfText