import sys
import os
from fontParts.world import *
import error

class Options(object):
    """
        impolements options to the script
    """
    def __init__(self):
        pass





def getFilesFromMainArg(mianArg):
    """
        Checks if the main argument is single ufo file
        or directory that contains multiple ufo files,
        then it returns list of the names of ufo fules
    """

    ufosNames = []
    if mianArg.split('.')[-1] == "ufo":

        error.fatal((mianArg in os.listdir('.')), "wrong file name")
        ufosNames = [mainArg]
        return ufosNames
    else:
        folder = os.listdir("./{}".format(mianArg))
        for file in folder:
            if file.split('.')[-1] == "ufo":
                ufosNames.append(file)

        return ufosNames

def getFonts(mianArg):
    fontNames = getFilesFromMainArg(mainArg)
    fonts = []
    if len(fontNames) > 1:
        for fontName in fontNames:
            font = OpenFont("./{}/{}".format(mainArg, fontName))
            fonts.append(font)
    else:
        font = OpenFont("./{}".format(mainArg))
        fonts.append(font)
    return fonts

def getFamilyNames(fonts):
    """
        returns names of families that where passed to the script
    """
    families = []

    countError = 1
    for font in fonts:
        # I don't know if this warning is necessary here (it prints out stuff in data-connected-method):
        error.warning((font.info.familyName!=None), "Ufo without FAMILY Name", countError=countError)
        if (font.info.familyName==None): countError += 1

        families.append(font.info.familyName)

    return tuple(set(families))

def getStyleNames(fonts,familyName):
    """
        returns names of styles for given familyName
    """
    styleNames = []

    countError = 1
    for font in fonts:
        if font.info.familyName == familyName:
            # I don't know if this warning is necessary here (it prints out stuff in data-connected-method):
            error.warning((font.info.styleName!=None), "Family contains STYLE without the Name",countError=countError)
            if (font.info.familyName==None): countError += 1

            styleNames.append(font.info.styleName)
    return styleNames

def printStyleNames(fonts):
    """
        prints in the command line lists of styles passed to the script
    """
    familyNames = getFamilyNames(fonts)

    for familyName in familyNames:
        print("Family Name: {}".format(familyName))
        print( "------------" )
        styleNames = getStyleNames(fonts,familyName)
        for styleName in styleNames:

            print(" Style Name: {}".format(styleName))
        print("\n****\n")

def isStyleObliqueOrItalic(font):
    if font.info.italicAngle != 0 or None: # Maybe only None?
        return True
    else:
        return False




def main():
    fonts = getFonts(mainArg)
    printStyleNames(fonts)

if __name__ == "__main__":
    commands = (sys.argv)[1:-1]
    mainArg = (sys.argv)[-1]
    main()
