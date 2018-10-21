"""  TEST OF PDF CONVERTER
"""

from pdfConverter import PDFConverter
import os


# Test PDF Location string
testFileDir = ("./../TestPDF/math151.pdf")

# prints the file location
print(testFileDir)

# creates a new instance of a pdf converter
conv = PDFConverter(testFileDir)

# gets the text
text = conv.getText()

# prints out the text
print(text)

"""
 END TEST OF PDF CONVERTER
"""




"""  TEST OF IMG CONVERTER
"""
from .imgConverter import IMGconverter
import os


# Test PDF Location string
testFileDir = ("./../TestPDF/TestPDF-1.jpg")

# prints the file location
print(testFileDir)

# creates a new instance of a pdf converter
conv = IMGconverter(testFileDir)

# gets the text
text = conv.getText()
# prints out the text
print(text)


""" END TEST OF IMG CONVERTER
"""

"""  TEST OF DOC CONVERTER
"""
from docConverter import DOCconverter


# Test PDF Location string
testFileDir = ("./../TestPDF/testDoc2.doc")

# prints the file location
print(testFileDir)

# creates a new instance of a pdf converter
conv = DOCconverter(testFileDir)

# gets the text
text = conv.getText()

# prints out the text
print(text)


""" END TEST OF DOC CONVERTER
"""



"""  TEST OF TXT CONVERTER
"""
from converters.textConverter import TXTconverter


# Test PDF Location string
testFileDir = ("./../TestPDF/testTXT.txt")

# prints the file location
print(testFileDir)

# creates a new instance of a pdf converter
conv = DOCconverter(testFileDir)

# gets the text
text = conv.getText()

# prints out the text
print(text)


""" END TEST OF DOC CONVERTER
"""
