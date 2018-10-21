from __future__ import print_function
import sys
import zerorpc
from google.cloud import vision
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import io
import docxpy
import datefinder
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# This is the class that will parse stuff.
class BackendApi(object):

    # Returns whatever text you pass it for testing
    def echo(self, text):
        return text

    # TODO: Create method that grabs email address
    def transmitData(self, filesString=""):
        print(filesString)
        parse = FileParser(filesString)

        return "Finished Parsing"



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
class CalendarPush:
    def __init__(self, Tests):
        print()


        store = file.Storage('backend/token.json')
        creds = store.get()
        

        if not creds or creds.invalid:
          flags = tools.argparser.parse_args(args=[])
          flow = client.flow_from_clientsecrets('backend/CalCred.json', SCOPES)
          creds = tools.run_flow(flow, store, flags)

        service = build('calendar', 'v3', http=creds.authorize(Http()))

        #Open URL


        # Call the Calendar API
        for eventObject in Tests:
            event = {
              'summary': str("Test for " + eventObject.getClass()),
              'description': str(eventObject.getDescription()),
              'start': {
                "date": str(eventObject.getDate()),
              },
              'end': {
                'date': str(eventObject.getDate()),
              },
              'reminders': {
                'useDefault': False,
                'overrides': [
                  {'method': 'email', 'minutes': 24 * 60},
                  {'method': 'popup', 'minutes': 10},
                ],
              },
            }
            # print(event)


            event = service.events().insert(calendarId='primary', body=event).execute()


            print ('Event created: %s' % (event.get('htmlLink')))



class DOCconverter:

    # text
    docText = ""

    # Given a link to a Document location, convert it to a string.
    # Returns a string of all the text in a Image Document
    # Max length string is as long mem will allows.
    """Detects text in the file."""
    def docToText(self, path):
        text = docxpy.process(path)
        print(text)
        return text

    # linkToIMG is a link to DOC
    def __init__(self, linkToDOC):
        # The text extracted from a Document, with some formatting
        self.docText = self.docToText(linkToDOC)


    def getText(self):
        return self.docText



class IMGconverter:

    # text
    imgText = ""

    # Given a link to a Image location, convert it to a string.
    # Returns a string of all the text in a Image Document
    # Max length string is as long mem will allows.
    """Detects text in the file."""
    def imgToText(self, path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.dirname(os.path.realpath(__file__)) + "./../backend/credentialFile.json"
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.document_text_detection(image=image)
        texts = response.text_annotations

        testOutput = ('{}'.format(response.full_text_annotation.text))
        return testOutput

    # linkToIMG is a link to IMG
    def __init__(self, linkToIMG):
        # The text extracted from a pdf, with some formatting
        self.imgText = self.imgToText(linkToIMG)


    def getText(self):
        return self.imgText


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



class TXTconverter:

    # text
    fileText = ""

    # Given a link to a txt file location, convert it to a string.
    # Returns a string of all the text in a Image Document
    # Max length string is as long mem will allows.
    """Detects text in the file."""
    def txtToText(self, path):
        data = ""
        with open(path, 'r') as myfile:
            data=myfile.read().replace('\n', ' ')
        print(data)
        return data

    # linkToIMG is a link to txt
    def __init__(self, linkToTXT):
        # The text extracted from a txt file, with some formatting
        self.fileText = self.txtToText(linkToTXT)


    def getText(self):
        return self.fileText






class Test:

    # The date of test
    # TODO: Change to datetime
    testDate = None

    # Test Descript
    testDescription = ""

    # Test Class #WIP
    testClass = ""

    def __init__(self, date, description):
        self.testDate = date
        self.testDescription = description
        self.testClass = "TBA"

    def getDescription(self):
        return self.testDescription

    def getDate(self):
        return self.testDate
    
    def getClass(self):
        return self.testClass



class FileParser:
    # List of all tests
    tests = []

    # Files
    filePaths = []

    # email
    # email = ""

    def __init__(self, files) :
        self.filePaths = files.split(",")
        # self.email = emailText

        for file in self.filePaths:
            self.docChoose(file)


        calendar = CalendarPush(self.tests)


    def docChoose(self, filePath):
        if( filePath.endswith(".pdf") ):
            conv = PDFConverter(filePath)
            outputText = conv.getText()

            self.stringSplit(outputText)

        # Bunch of image tupes
        elif( filePath.endswith(".jpg") or filePath.endswith(".png") or filePath.endswith(".tif") or filePath.endswith(".jpeg") ):
            conv = IMGconverter(filePath)
            outputText = conv.getText()

            self.stringSplit(outputText)
        
        # Docs
        elif( filePath.endswith(".docx")):
            conv = DOCconverter(filePath)
            outputText = conv.getText()

            self.stringSplit(outputText)

        # Txt
        elif(filePath.endswith(".txt")):
            conv = TXTconverter(filePath)
            outputText = conv.getText()

            self.stringSplit(outputText)
        else:
            print("YOUR FORMAT SUCKS AND YOU SUCK AS WELL")


    def stringSplit(self, orig):
        # List of days of the week (tamper with the date)
        daysOfWeek = ["Monday,", "Tuesday,", "Wednesday,", "Thursday,", "Friday,"]

        # replace diff with variable that holds the actual text string
        splitString = orig.split(".")
        for sentence in splitString:
            finalString = ""
            newsplitString = sentence.split(" ")
        for letters in newsplitString:
            if letters in daysOfWeek:
                continue
            elif letters.find(",") >= 0:
                # print("found a comma" , i)
                letters = letters.replace(",", ",...............")
                # print("new i ", i)
            elif letters.find(":") >= 0:
                # print("found a colon" , i)
                letters = letters.replace(":", "...")
                # print("new i ", i)
            finalString += (letters + " ")

        # FInds all dates in the file
        matches = datefinder.find_dates(finalString)



        # Matches the dates with a sentence.
        for match in matches:
            temp = Test(match.date(), sentence)

            self.tests.append(temp)

    def getTests(self):
        return self.tests






def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(BackendApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()



if __name__ == '__main__':
    main()





