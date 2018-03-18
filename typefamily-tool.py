#!/usr/bin/env python
from misc.Output import execute_MAIN_STRING
import os
import sys
from FUNC import error
from fontParts.world import *
from DOCS.FamilyInfo import *


class Options(object):
    ###IMPOLEMENT THIS!
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

        error.fatal(not (os.path.isfile(mainArg)), "wrong file name")
        ufosNames = [mainArg]
        return ufosNames
    else:
        error.fatal((os.path.exists(mainArg)),
                    "No such file or directory: '{}'".format(mainArg))
        folder = os.listdir("{}".format(mianArg))
        for file in folder:
            if file.split('.')[-1] == "ufo":
                ufosNames.append(file)

        return ufosNames


def getFonts(mianArg):
    fontNames = getFilesFromMainArg(mainArg)
    fonts = []
    if len(fontNames) > 1:
        for fontName in fontNames:
            font = OpenFont("{}/{}".format(mainArg, fontName))
            fonts.append(font)
    else:
        font = OpenFont("./{}".format(mainArg))
        fonts.append(font)
    return fonts



def main():
    MAIN_STRING = ""
    fonts = getFonts(mainArg)
    MAIN_STRING = nameChecker(fonts,MAIN_STRING)


    execute_MAIN_STRING(MAIN_STRING)
    # printStyleNames(fonts)


if __name__ == "__main__":
    import sys
    commands = (sys.argv)[1:-1]
    mainArg = (sys.argv)[-1]
    main()
