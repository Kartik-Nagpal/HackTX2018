
from testObject import Test
from parsing import FileParser
from api import BackendApi


filepath = "C:/Users/Angelo/Desktop/HackTX/TestPDF/chem107.pdf"

# temp = FileParser(filepath)

BackendApi.transmitData(filepath)

# print(temp.getTests()[0].getDescription())