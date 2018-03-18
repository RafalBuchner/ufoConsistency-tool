# -*- coding: utf-8 -*-
#!/usr/bin/env python
from misc.Output import execute_MAIN_STRING
import os
import sys
from FUNC import error

from DOCS.FamilyInfo import *


# class Options(object):
#     ###IMPOLEMENT THIS!
#     """
#         impolements options to the script
#     """
#
#     def __init__(self):
#         pass


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
    txt = ""
    ###TESTS:
    txt += u"_______TEST_______\n"
    setup = Setup(commands, mainArg)
    txt += setup.getTxt()
    MAIN_STRING = txt
    execute_MAIN_STRING(MAIN_STRING)


if __name__ == "__main__":
    import sys
    commands = (sys.argv)[1:-1]
    mainArg = (sys.argv)[-1]
    # mainArg = "diff-masters"
    main()
