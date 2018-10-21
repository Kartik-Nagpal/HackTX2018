from google.cloud import vision
import os
import io

# TODO: Image text sometimes can't read tables properly.

class IMGconverter:

    # text
    imgText = ""

    # Given a link to a Image location, convert it to a string.
    # Returns a string of all the text in a Image Document
    # Max length string is as long mem will allows.
    """Detects text in the file."""
    def imgToText(self, path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.dirname(os.path.realpath(__file__)) + "./credentialFile.json"
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
