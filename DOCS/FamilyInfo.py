"""
    TODO:
    NameChecker needs to follow full OpenType spects when it comes to naming font
"""

from misc.TableStringMD import *
from misc.Output import output
import misc.letterMachine as lettMachine
import FUNC.error as error
import time  # Can I do it in different way? On lower level of the implementation?


def getFamilyNames(fonts):
    """
        returns names of families that where passed to the script
    """
    families = []

    countError = 1
    for font in fonts:

        families.append(font.info.familyName)

    return list(set(families))


def getStyleNames(fonts, familyName):
    """
        returns names of styles for given familyName
    """
    styleNames = []

    countError = 1
    for font in fonts:
        if font.info.familyName == familyName:
            if (font.info.familyName == None):
                countError += 1

            styleNames.append(font.info.styleName)
    return styleNames


def nameChecker(fonts, MAIN_STRING):
    """
        Checks if opened fonts has none name as
        familyName, styleName
        TODO: check OTF spects for naming, and add to it
    """
    def _warning(txt, condition, MAIN_STRING, font, countError):
        MAIN_STRING = error.warning(condition,
                                    txt, MAIN_STRING=MAIN_STRING, countError=countError)
        MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
            font.path.split("/")[-1])

        return MAIN_STRING

    def _consider(txt, font,  MAIN_STRING):
        MAIN_STRING = error.consider(txt, MAIN_STRING)
        MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
            font.path.split("/")[-1])
        return MAIN_STRING

    MAIN_STRING += "## UFO-family-tool\n------------------\n# **Name Check**\n"
    MAIN_STRING += "```\n"
    countErrorFamilyName = 0
    countErrorStyleName = 0
    countErrorPsFontName = 0
    familyNames = getFamilyNames(fonts)
    styleNames = []
    fontCount = 1
    for font in fonts:
        MAIN_STRING += " - font `#{}` from total `{}`\n".format(fontCount, len(fonts))
        # check nameID 1,2
        for familyName in familyNames:

            styleNames += getStyleNames(fonts, familyName)

            if font.info.familyName == familyName:
                if font.info.familyName == None:
                    MAIN_STRING = _warning(
                        "Ufo without **FamilyNameERROR: Family Name**", (font.info.familyName != None), MAIN_STRING, font, countErrorFamilyName + 1)
                    countErrorFamilyName += 1

                if font.info.styleName == None:
                    MAIN_STRING = _warning("StyleNameERROR: Family *'{}'* contains **Style without the Name**".format(
                        familyName), (font.info.styleName != None), MAIN_STRING, font, countErrorStyleName + 1)
                    countErrorStyleName += 1
        # TODO check nameID 3 (copyright)
        # TODO check nameID 4 (full name, space separated, only ascii)

        # check nameID6
        # TODO: check if PSfontName is built from familyName and styleName
        psFontName = font.info.postscriptFontName
        if psFontName:
            if len(psFontName.split("-")) == 1:
                MAIN_STRING = _consider("PostscriptFontNameERROR: could be a wrong **Postscript Font Name** *'{}'* ( No Separation or separated without the dashes). \n            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic".format(
                    psFontName), font,  MAIN_STRING)


            if not len(psFontName) < 63:
                MAIN_STRING = _warning("PostscriptFontNameERROR: UFO has wrong **Postscript Font Name** *'{}'* ( more than 63 characters)".format(
                    psFontName), (len(psFontName) < 63), MAIN_STRING, font, countErrorPsFontName + 1)
                countErrorPsFontName += 1

            for char in psFontName:
                if char not in lettMachine.ASCIInaming:
                    MAIN_STRING = _warning("PostscriptFontNameERROR: UFO has wrong **Postscript Font Name** *'{}'* ( non ASCII character - {})".format(
                        psFontName, char), not(char not in lettMachine.ASCIInaming), MAIN_STRING, font, countErrorPsFontName + 1)
                    countErrorPsFontName += 1

        else:
            MAIN_STRING = _warning("PostscriptFontNameERROR: UFO has **Postscript Font Name** set to None".format(
                psFontName), (psFontName != None), MAIN_STRING, font, countErrorPsFontName + 1)
            countErrorPsFontName += 1
        ##
        fontCount += 1
    # MAIN_STRING += "```\n"

    # Printing Summary
    MAIN_STRING += "\n## Summary\n"
    # Numbers of errors
    MAIN_STRING += "\n> - {} - number of different family names\n".format(
        len(familyNames))
    MAIN_STRING += "\n> - {} - number of Family Name errors\n".format(
        countErrorFamilyName)
    MAIN_STRING += "\n> - {} - number of Style Name errors\n".format(
        countErrorStyleName)
    MAIN_STRING += "\n> - {} - number of Postscript Name errors\n".format(
        countErrorPsFontName)

    MAIN_STRING += "\n### Structure:\n"
    MAIN_STRING = printStyleNames(fonts, MAIN_STRING)
    return MAIN_STRING


def printStyleNames(fonts, MAIN_STRING):
    """
        prints in the command line lists of styles passed to the script
    """
    familyNames = getFamilyNames(fonts)

    # for familyName in familyNames:
    #     styleNames = getStyleNames(fonts, familyName)
    #     for styleName in styleNames:
    #
    #         MAIN_STRING += " Style Name: {}".format(styleName))
    #     MAIN_STRING += "\n****\n"
    rows = [getStyleNames(fonts, familyName) for familyName in familyNames]
    lineInfo = ["style #{}".format(i) for i in range(
        len(max(rows, key=lambda coll: len(coll))))]
    table = TableStringMD(
        [x for x in rows], rowInfo=familyNames, lineInfo=lineInfo)
    for line in table.getTableListMD():
        MAIN_STRING += line + "\n"
    return MAIN_STRING


def isStyleObliqueOrItalic(font):
    if font.info.italicAngle != 0 or None:  # Maybe only None?
        return True
    else:
        return False
