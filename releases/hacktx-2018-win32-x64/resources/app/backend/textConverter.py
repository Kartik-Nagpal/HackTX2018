import os
import io

# TODO: Document table text sometimes doesn't return.

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
