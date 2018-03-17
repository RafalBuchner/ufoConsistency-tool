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

def nameChecker(fonts):
    """
        Checks if opened fonts has none name as
        familyName, styleName
        TODO: check OTF spects for naming, and add to it
    """
    output("## UFO-family-tool\n------------------\n# **Name Check**\n```")
    countErrorFamilyName = 0
    countErrorStyleName = 0
    countErrorPsFontName = 0
    familyNames = getFamilyNames(fonts)
    styleNames = []
    fontCount = 1
    for font in fonts:
        output("> font #{} from total {}".format(fontCount, len(fonts)))
        # output("font #{} from total {}".format(fontCount, len(fonts)))
        for familyName in familyNames:

            styleNames += getStyleNames(fonts, familyName)

            if font.info.familyName == familyName:
                if font.info.familyName == None:
                    output("```")
                    error.warning((font.info.familyName != None),
                                  "Ufo without **Family Name**", countError=countErrorFamilyName+1)
                    output("\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1]))
                    output("```")
                    countErrorFamilyName += 1

                if font.info.styleName == None:
                    output("```")
                    error.warning((font.info.styleName != None),
                    "Family '{}' contains **Style without the Name**".format(familyName), countError=countErrorStyleName+1)
                    output("\\\\\\\\\\\\\\\ *FILE NAME: {}*".format(font.path.split("/")[-1]))
                    output("```")
                    countErrorStyleName += 1

        psFontName = font.info.postscriptFontName
        if psFontName:
            if len(psFontName.split("-")) == 1:
                output("```")
                error.warning((len(psFontName.split("-")) != 1),
                "UFO has wrong **Postscript Font Name** '{}' ( seperated without dashes)".format(psFontName), countError=countErrorPsFontName+1)
                output("\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1]))
                output("```")
        else:
            output("```")
            error.warning((psFontName != None),
            "UFO has **Postscript Font Name** set to None".format(psFontName), countError=countErrorPsFontName+1)
            output("\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(font.path.split("/")[-1]))
            output("```")
        ##
        fontCount += 1
    output("```")

    # Printing Summary
    output("\n## Summary")
    # Numbers of errors
    output("\n> - {} - number of different family names".format(len(familyNames)))
    output("\n> - {} - number of family names set to None".format(countErrorFamilyName))
    output("\n> - {} - number of style names set to None".format(countErrorStyleName))

    output("\n### Structure:")
    printStyleNames(fonts)






def printStyleNames(fonts):
    """
        prints in the command line lists of styles passed to the script
    """
    familyNames = getFamilyNames(fonts)

    # for familyName in familyNames:
    #     styleNames = getStyleNames(fonts, familyName)
    #     for styleName in styleNames:
    #
    #         output(" Style Name: {}".format(styleName))
    #     output("\n****\n")
    rows = [getStyleNames(fonts, familyName) for familyName in familyNames]
    lineInfo = ["style #{}".format(i) for i in range(len(max(rows, key=lambda coll: len(coll))))]
    table = TableStringMD([x for x in rows],rowInfo=familyNames,lineInfo=lineInfo)
    for line in table.getTableListMD():
        output(line)


def isStyleObliqueOrItalic(font):
    if font.info.italicAngle != 0 or None:  ###Maybe only None?
        return True
    else:
        return False
