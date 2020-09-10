from PIL import Image
import numpy as np


def verifyType(image):
    """Verifies the image selected matches accepted file types"""
    acceptedTypes = ["bmp", "raw", "png"]
    fileExt = image[-3:]
    if fileExt not in acceptedTypes:
        print("\nImage must be RAW, PNG, or BMP type")
        return False
    else:
        return True


def getSource():
    """Requests full path to an image from the user"""
    while True:
        sourceImage = input("Image file path: ")
        if verifyType(sourceImage):
            try:
                imageFile = Image.open(sourceImage)
            except FileNotFoundError:
                print("File not found\n")
            else:
                imageData = np.array(imageFile)
                return imageData


def getContext(data):
    """Retrieves the center row of pixel data to be used for password generation"""
    centerRow = len(data) // 2
    centerRow = data[centerRow]
    return centerRow


def verifyComplexity(data):
    """Determines whether an image is visually complex enough for secure password
    generation. If the image deminsions are too small, or the image does not contain
    sufficient color complexity, the user must select a new image"""
    weakCount = 0
    if len(data) > 128:
        for pixelRow in range(len(data)):
            currentRow = data[pixelRow]
            comparison = currentRow == data[0]
            same = comparison.all()
            if same:
                weakCount += 1
        if weakCount > 48:
            print("Image must be more visually complex for password generation\n")
            return False
        else:
            return True
    else:
        print("Image must be more visually complex for password generation\n")
        return False


def diffPass():
    """Asks the user whether they would like to input another
    image for password generation"""
    while True:
        again = input("Generate another password? [Y / N]: ")
        if again.upper() not in ['Y', 'N']:
            print("Please enter Y or N to continue\n")
        else:
            return again.upper()
