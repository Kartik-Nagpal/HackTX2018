import os
import io
import docxpy

# TODO: Document table text sometimes doesn't return.

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
