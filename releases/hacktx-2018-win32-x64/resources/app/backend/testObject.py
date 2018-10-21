# This is a test class
class Test:

    from datetime import datetime

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

