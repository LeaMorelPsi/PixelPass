import Collection
import GenPass


if __name__ == "__main__":

    # Initialize variable for master modification value
    masterMod = ''

    # Select master image to produce modification value
    while True:
        print("\nSelect master image_")
        masterImage = Collection.getSource()
        if Collection.verifyComplexity(masterImage):
            masterSource = Collection.getContext(masterImage)
            masterAvgs = GenPass.getAverages(masterSource)
            masterMod = GenPass.masterModifier(masterAvgs)
            break

    # Select image and generate password
    while True:
        print("\nSelect password key image_")
        sourceImage = Collection.getSource()
        if Collection.verifyComplexity(sourceImage):
            passSource = Collection.getContext(sourceImage)
            averages = GenPass.getAverages(passSource)
            maxLength = GenPass.getMaxPass(averages)
            passLength = GenPass.passwordLength(maxLength)
            avgChunks = GenPass.defineChunks(
                averages, maxLength, passLength)
            passValues = GenPass.getAverages(avgChunks)
            password = GenPass.genPass(passValues, masterMod)
            print("\nPassword:\n\n" + str(password) + "\n\n")
        if Collection.diffPass() != 'Y':
            break
