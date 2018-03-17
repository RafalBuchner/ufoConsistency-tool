import sys
import os
from fontParts.world import *



def fatalError(expression, string):
    """
        Error for command prompt
    """
    if not expression:  # FATAL ERROR???
        sys.exit(f"[FATAL ERROR]//> {string}")

def warning(expression, string, countError=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """
    if countError != None:
        if not expression:  # WARNING ERROR???
            print(f"[WARNING]//> {string} > {countError}")
    else:
        if not expression:  # WARNING ERROR???
            print(f"[WARNING]//> {string}")



def getFilesFromMainArg(mianArg):
    """
        Checks if the main argument is single ufo file
        or directory that contains multiple ufo files,
        then it returns list of the names of ufo fules
    """

    ufosNames = []
    if mianArg.split('.')[-1] == "ufo":

        fatalError((mianArg in os.listdir('.')), "wrong file name")
        ufosNames = [mainArg]
        return ufosNames
    else:
        folder = os.listdir(f"./{mianArg}")
        for file in folder:
            if file.split('.')[-1] == "ufo":
                ufosNames.append(file)

        return ufosNames

def getFonts(mianArg):
    fontNames = getFilesFromMainArg(mainArg)
    fonts = []
    if len(fontNames) > 1:
        for fontName in fontNames:
            font = OpenFont(f"./{mainArg}/{fontName}")
            fonts.append(font)
    else:
        font = OpenFont(f"./{mainArg}")
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
        warning((font.info.familyName!=None), "Ufo without FAMILY Name", countError=countError)
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
            warning((font.info.styleName!=None), "Family contains STYLE without the Name",countError=countError)
            if (font.info.familyName==None): countError += 1

            styleNames.append(font.info.styleName)
    return styleNames

def printStyleNames(fonts):
    """
        prints in the command line lists of styles passed to the script
    """
    familyNames = getFamilyNames(fonts)

    for familyName in familyNames:
        print(f"Family Name: {familyName}")
        print( "------------" )
        styleNames = getStyleNames(fonts,familyName)
        for styleName in styleNames:

            print(f" Style Name: {styleName}")
        print("\n****\n")

if __name__ == "__main__":
    commands = (sys.argv)[1:-1]
    mainArg = (sys.argv)[-1]
    print(sys.path)
    # fonts = getFonts(mainArg)

    # printStyleNames(fonts)
