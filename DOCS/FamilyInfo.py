"""
    TODO:
    NameChecker needs to follow full OpenType spects when it comes to naming font
"""

from misc.TableStringMD import *
from misc.Output import output
import FUNC.error as error
import time ###Can I do it in different way? On lower level of the implementation?




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

def nameChecker(fonts,MAIN_STRING):

    """
        Checks if opened fonts has none name as
        familyName, styleName
        TODO: check OTF spects for naming, and add to it
    """
    def _warning(txt,condition,MAIN_STRING,font,countError):
        MAIN_STRING += "```\n"
        MAIN_STRING = error.warning(condition,
        txt, MAIN_STRING=MAIN_STRING, countError=countError)
        MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1])
        MAIN_STRING += "```\n"
        return MAIN_STRING



    MAIN_STRING += "## UFO-family-tool\n------------------\n# **Name Check**\n```\n"
    countErrorFamilyName = 0
    countErrorStyleName = 0
    countErrorPsFontName = 0
    familyNames = getFamilyNames(fonts)
    styleNames = []
    fontCount = 1
    for font in fonts:
        MAIN_STRING += "> font #{} from total {}\n".format(fontCount, len(fonts))
        # MAIN_STRING += "font #{} from total {}\n".format(fontCount, len(fonts))
        for familyName in familyNames:

            styleNames += getStyleNames(fonts, familyName)

            if font.info.familyName == familyName:
                if font.info.familyName == None:
                    MAIN_STRING = _warning("Ufo without **Family Name**",(font.info.familyName != None),MAIN_STRING,font,countErrorFamilyName+1)

                    countErrorFamilyName += 1

                if font.info.styleName == None:
                    _warning("Family '{}' contains **Style without the Name**".format(familyName),(font.info.styleName != None),MAIN_STRING,font,countErrorStyleName+1):
                    countErrorStyleName += 1

        psFontName = font.info.postscriptFontName
        if psFontName:
            if len(psFontName.split("-")) == 1:
                MAIN_STRING += "```\n"
                MAIN_STRING = error.warning((len(psFontName.split("-")) != 1),
                "UFO has wrong **Postscript Font Name** '{}' ( seperated without dashes)".format(psFontName), MAIN_STRING=MAIN_STRING, countError=countErrorPsFontName+1)
                MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1])
                MAIN_STRING += "```\n"
            if len(psFontName) > 63:
                MAIN_STRING += "```\n"
                MAIN_STRING = error.warning((len(psFontName.split("-")) != 1),
                "UFO has wrong **Postscript Font Name** '{}' ( seperated without dashes)".format(psFontName), MAIN_STRING=MAIN_STRING, countError=countErrorPsFontName+1)
                MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1])
                MAIN_STRING += "```\n"
        else:
            MAIN_STRING += "```\n"
            MAIN_STRING = error.warning((psFontName != None),
            "UFO has **Postscript Font Name** set to None".format(psFontName), MAIN_STRING=MAIN_STRING, countError=countErrorPsFontName+1)
            MAIN_STRING += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1])
            MAIN_STRING += "```\n"
        ##
        fontCount += 1
    MAIN_STRING += "```\n"

    # Printing Summary
    MAIN_STRING += "\n## Summary\n"
    # Numbers of errors
    MAIN_STRING += "\n> - {} - number of different family names\n".format(len(familyNames))
    MAIN_STRING += "\n> - {} - number of family names set to None\n".format(countErrorFamilyName)
    MAIN_STRING += "\n> - {} - number of style names set to None\n".format(countErrorStyleName)

    MAIN_STRING += "\n### Structure:\n"
    MAIN_STRING = printStyleNames(fonts,MAIN_STRING)
    return MAIN_STRING






def printStyleNames(fonts,MAIN_STRING):
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
    lineInfo = ["style #{}".format(i) for i in range(len(max(rows, key=lambda coll: len(coll))))]
    table = TableStringMD([x for x in rows],rowInfo=familyNames,lineInfo=lineInfo)
    for line in table.getTableListMD():
        MAIN_STRING += line + "\n"
    return MAIN_STRING


def isStyleObliqueOrItalic(font):
    if font.info.italicAngle != 0 or None:  ###Maybe only None?
        return True
    else:
        return False
