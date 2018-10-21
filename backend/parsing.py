import datefinder

from .testObject import Test
from .pdfConverter import PDFConverter
from .imgConverter import IMGconverter
from .docConverter import DOCconverter
from .textConverter import TXTconverter
from .calendarLocal import CalendarPush
# TODO: Add comments

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