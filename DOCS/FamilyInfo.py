from misc.TableStringMD import *
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
    print("## UFO-family-tool\n------------------\n# **Name Check**")
    countErrorFamilyName = 0
    countErrorStyleName = 0
    familyNames = getFamilyNames(fonts)
    styleNames = []
    fontCount = 1
    for font in fonts:
        print("<br>> font #{} from total {}".format(fontCount, len(fonts)))
        time.sleep(0.05)
        # print("font #{} from total {}".format(fontCount, len(fonts)))
        for familyName in familyNames:

            styleNames += getStyleNames(fonts, familyName)

            if font.info.familyName == familyName:
                if font.info.familyName == None:
                    error.warning((font.info.familyName != None),
                                  "Ufo without FAMILY Name", countError=countErrorFamilyName+1)
                    print("<br>>            *FILE NAME: {}*\n".format(font.path.split("/")[-1]))
                    countErrorFamilyName += 1

                if font.info.styleName == None:
                    error.warning((font.info.styleName != None),
                    "Family '{}' contains STYLE without the Name".format(familyName), countError=countErrorStyleName+1)
                    print("<br>>            *FILE NAME: {}*".format(font.path.split("/")[-1]))
                    countErrorStyleName += 1
        fontCount += 1

    # Printing Summary
    print("## Summary")
    # Numbers of errors
    print("""
> - {} - number of different family names

> - {} - number of family names set to None

> - {} - number of style names set to None

          """.format(len(familyNames), countErrorFamilyName, countErrorStyleName, familyNames, styleNames))

    print("### Families:")
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
    #         print(" Style Name: {}".format(styleName))
    #     print("\n****\n")
    rows = [getStyleNames(fonts, familyName) for familyName in familyNames]
    lineInfo = ["style names"]+["--*--" for x in range(len(max(rows, key=lambda coll: len(coll)))-1)]
    table = TableStringMD([x for x in rows],rowInfo=familyNames,lineInfo=lineInfo)
    print(table.getTableStringMD())


def isStyleObliqueOrItalic(font):
    if font.info.italicAngle != 0 or None:  ###Maybe only None?
        return True
    else:
        return False
