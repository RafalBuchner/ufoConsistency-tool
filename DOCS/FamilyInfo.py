# -*- coding: utf-8 -*-
"""
    TODO:
    NameChecker needs to follow full OpenType spects when it comes to naming font


    methods naming system:
    name_Test() - returns string
    name_Check() - returns boolean

"""
from fontParts.world import *
import os
from misc.TableStringMD import *
from misc.Output import output
import misc.letterMachine as lettMachine
import FUNC.error as error
import time  # Can I do it in different way? On lower level of the implementation?
import misc.logic_func as logic

class About(object):
    def __init__(self):
        self.name = "UFO Consistency Tool"
        self.version = 0.001
        self.author = "Rafał Buchner"
        self.date = "03/2018"
        self.url = "https://github.com/RafalBuchner/ufoConsistency-tool"
        self.licence = "MIT"

    def getInfo(self):
        txt = """
```
version: {}
name: {}
author: {}
date: {}
licence type: {}
```
[github link]({})
""".format(
self.version,
self.name,
self.author,
self.date,
self.licence,
self.url
)
        return txt

    def help(self, isMarkdown=False):
        txt = ""
        # lineInfo = ["style #{}".format(i) for i in range(len(max(rows, key=lambda coll: len(coll))))]
        rowInfo = ['command','description']
        rows = [
        ['`-hmd`','`-h`','`-v`','`-n`','`-dev`'],
            [
                'Help formated for MarkDown output.',
                'Help formated for terminal output.',
                'Prints out version number and other information about {}.'.format(self.name),
                'Name Test, that prints out the analize of naming in given UFO files.',
                'Developer Test (stuff for experimenting within package) ### add more info later.'
            ]
        ]

        table = TableStringMD([x for x in rows], rowInfo=rowInfo)


        txt += '\n# {} HELP\n---\n'.format(self.name) # Title

        if isMarkdown:
            txt +=  table.getTableListMD()
        else:
            txt +="""
`-hmd` - Help formated for MarkDown output.
`-h`   - Help formated for terminal output.
`-v`   - Prints out version number and other information about {}.
`-n`   - Name Test, that prints out the analize of naming in given UFO files.
`-dev` - Developer Test (stuff for experimenting within package) ### add more info later.

""".format(self.name)



        return txt






class Setup(object):

    def __init__(self, commands, mainArg):
        self.txt = ""
        self.mainArg = mainArg
        self.commands = commands
        self.fonts = self.getFonts()
        self.test = FolderTest(self.fonts)

        self.commandsExecution()





    def commandsExecution(self):
        for option in self.commands:

            if option == "-h":
                self.txt += About().help()
            if option == "-hmd":
                self.txt += About().help(True)

            elif option == "-v":
                self.txt += About().getInfo()

            elif option == "-n":
                self.txt += self.test.name_Test()
            elif option == "-dev":
                test_playground = TestClass(self.test, self.fonts)
                self.txt += test_playground.testString()

            else:
                msg = "`command like:'{}' doesn't exist`".format(option)
                error.fatal(False, msg)

    def getTxt(self):
        return self.txt

    def getFonts(self):
        mainArg = self.mainArg

        def _getFilesFromMainArg(mianArg):
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

        fontNames = _getFilesFromMainArg(mainArg)
        fonts = []
        if len(fontNames) > 1:
            for fontName in fontNames:
                font = OpenFont("{}/{}".format(mainArg, fontName))
                fonts.append(font)
        else:
            font = OpenFont("./{}".format(mainArg))
            fonts.append(font)
        return fonts


class SingleFontTest(object):
    def __init__(self, font):
        self.font = font
        self._generateNames()

    def _generateNames(self):
        self.familyName = self.font.info.familyName
        self.styleName = self.font.info.styleName
        self.psFontName = self.font.info.postscriptFontName
        self.italicAngle = self.font.info.italicAngle

    def getFamilyName(self):
        return self.familyName

    def getStyleName(self):
        return self.styleName

    def familyName_Test(self):
        """
            name ID 1 - test if the name is set to None
        """
        txt = ""
        txt += error.warning(self.familyName != None,
                             "**FamilyNameERROR** > nameID 1: Ufo without Family Name",
                             self.font)
        if self.familyName != None:
            if len(self.familyName) < 63:
                txt += error.warning(len(self.familyName) < 63,
                              "**FamilyNameERROR** > nameID 1: UFO has wrong Family Name *'{}'* ( more than 63 characters)",
                                     self.font)
        return txt

    def styleName_Test(self):
        """
            name ID 2 - test if the name is set to None
        """
        txt = ""
        txt += error.warning(self.styleName != None,
                             u"**StyleNameERROR** > nameID 1: Ufo without Style Name (if absent then Name ID 2 () is considered to be the typographic style name)",
                             self.font)
        if self.styleName != None:
            if len(self.styleName) < 63:
                txt += error.warning(len(self.styleName) < 63,
                              u"**StyleNameERROR** > nameID 1: UFO has wrong Style Name *'{}'* ( more than 63 characters)",
                                     self.font)
        return txt

    def psFontName_Test(self):
        """
            name ID 6 - test if the name is set to None
        """
        txt = u""
        if self.psFontName:
            if len(self.psFontName.split("-")) == 1:
                txt += error.consider(u"**PostscriptFontNameERROR**: could be a wrong **Postscript Font Name** *'{}'* ( No Separation or separated without the dashes)".format(
                    self.psFontName),self.font)
                txt += u"\n            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic\n"

            if not len(self.psFontName) < 63:
                txt += error.warning(
                u"**PostscriptFontNameERROR**: UFO has wrong **Postscript Font Name** *'{}'* ( more than 63 characters)".format(self.psFontName),
                (len(self.psFontName) < 63),self.font)

            for char in self.psFontName:
                if char not in lettMachine.ASCIInaming:
                    txt += error.warning(
                    u"**PostscriptFontNameERROR**: UFO has wrong **Postscript Font Name** *'{}'* ( non ASCII character )".format(self.psFontName),
                    not(char not in lettMachine.ASCIInaming),self.font)
        return txt

    def isStyleObliqueOrItalic_Check(self):
        if self.italicAngle != 0 or None:  # Maybe only None?
            return True
        else:
            return False


class FolderTest(object):
    def __init__(self, fonts):
        self.fonts = fonts
        # self.txt = ""

    def getFamilyNames(self):
        """
        returns names of families that where passed to the script
        """
        families = []

        countError = 1
        for font in self.fonts:

            families.append(font.info.familyName)

        return list(set(families))

    def getStyleNames(self, familyName):
        """
            returns names of styles for given familyName
        """
        styleNames = []


        for font in self.fonts:
            if font.info.familyName == familyName:
                styleNames.append(font.info.styleName)

        return styleNames

    def name_Test(self):
        """
            Checks if opened fonts has none name as
            familyName, styleName
            TODO: check OTF spects for naming, and add to it
        """

        txt = u""
        countErrorFamilyName = 0
        countErrorStyleName = 0
        countErrorPsFontName = 0
        familyNames = self.getFamilyNames()
        styleNames = []
        fontCount = 1

        txt += "#### Ufo-test-tool: Name Test\n"
        txt += u"---\n"
        txt += "# Single font tests:\n"
        txt += u"```\n"
        for font in self.fonts:
            txt += u" - font `#{}` from total `{}`\n".format(
                fontCount, len(self.fonts))
            fontTest = SingleFontTest(font)
            styleNames.append(fontTest.styleName)
            for familyName in familyNames:
                #1
                if font.info.familyName == familyName:
                    txt += fontTest.familyName_Test()
                    #2
                    if font.info.styleName == None:
                        txt += fontTest.styleName_Test()
            # TODO check nameID 3 (copyright)
            # TODO check nameID 4 (full name, space separated, only ascii)
            # check nameID6
            # TODO: check if PSfontName is built from familyName and styleName

            #6
            txt += fontTest.psFontName_Test()

            fontCount += 1
        # MAIN_STRING += "```\n"
        # for styleSet in styleNames
        # Printing Summary
        txt += "\n## Summary\n"
        # Numbers of errors
        txt += "\n> - {} - number of different family names\n".format(
            len(familyNames))
        txt += "\n> - {} - number of different style names\n".format(
            len(styleNames))

        if len(self.fonts)>1:
            txt += "\n# Multiple fonts tests:\n TODO: \n - font names consistency across family\n - style names consisency across family\n - glyph names consistency across family\n - kerning pairs names consisency across family\n - kerning pairs names consisency across family\n"

        txt += "\n### Structure:\n"
        txt += self.printStyleNames_Table()


        return txt

    def printNumberOfGlyphs_Table(self):
        txt = ""
        txt += u"Number of glyphs in every font\n\n"

        familyNames = self.getFamilyNames()

        for familyName in familyNames:
            rows = []
            values = []
            for font in self.fonts:
                if font.info.familyName == familyName:
                    if familyName == None:
                        currFamilyName = u"FAMILY_NONE"
                    else:
                        currFamilyName = familyName
                    if font.info.styleName == None:
                        currStaleName = u"STYLE_NONE"
                    else:
                        currStaleName = font.info.styleName

                    rows.append([currFamilyName +" "+ currStaleName, len(font.glyphOrder)])
                    values.append(len(font.glyphOrder))
            isEqualGlyphNum = logic.equalElements_check(values)

            if not isEqualGlyphNum:
                rows.append([u"Error", "*NOT EQUAL NUMBER ACROSS THE FAMILY*"])



            lineInfo = [u"Family Name", "Glyphs Number"]
            table = TableStringMD([x for x in rows], lineInfo=lineInfo)
            txt += table.getTableListMD()
            txt += u"\n"
        return txt

    def differenceCharacterSet_test(self):
        txt = ""
        txt += "---------------------------------------\n"
        txt += "## Differences in Character Set\n"
        txt += "---------------------------------------\n"
        familyNames = self.getFamilyNames()
        for familyName in familyNames:
            glyphOrder_lengths = []
            for font in self.fonts:
                if font.info.familyName == familyName:
                    glyphOrder_lengths.append(len(font.glyphOrder))


            isEqualGlyphNum = logic.equalElements_check(glyphOrder_lengths)
            # print(familyName)
            # print(glyphOrder_lengths)
            txt += "### FAMILY **>{}<**\n".format(str(familyName).upper())
            if not isEqualGlyphNum:

                for font in self.fonts:
                    if font.info.familyName == familyName:

                        for otherFont in self.fonts:
                            if otherFont.info.familyName == familyName:
                                txt += " - DIFFERENCES BETWEEN FONT **{}** AND **{}**:\n".format(
                                                                                                    str(font.info.styleName).upper(),
                                                                                                    str(otherFont.info.styleName).upper())
                                difference = list(set(font.glyphOrder) - set(otherFont.glyphOrder))
                                txt += "         "
                                if len(difference) > 1:
                                    for glyphname in difference:
                                        comma = ", "
                                        if difference.index(glyphname)+1 == len(difference):
                                            comma = ""
                                        txt += glyphname + comma
                                else:
                                    txt += "-"
                                txt += "\n"

            txt += "\n"
        return txt
    def printStyleNames_Table(self):
        """
            prints in the command line lists of styles passed to the script
        """
        familyNames = self.getFamilyNames()

        rows = [self.getStyleNames(familyName) for familyName in familyNames]

        lineInfo = ["style #{}".format(i) for i in range(len(max(rows, key=lambda coll: len(coll))))]

        table = TableStringMD([x for x in rows], rowInfo=familyNames, lineInfo=lineInfo)

        table.rows[0][0] = "FAMILY NAME:"
        return table.getTableListMD()

class TestClass(object):
    def __init__(self, folderTest, fonts):
        self.folderTest = FolderTest(fonts)

    def testString(self):
        txt = ''
        txt += "---------------------------------------\n" ###TESTS
        txt += "# TEST\n" ###TESTS
        txt += "---------------------------------------\n" ###TESTS
        txt += self.folderTest.printStyleNames_Table()
        # txt += self.folderTest.printNumberOfGlyphs_Table()
        txt += self.folderTest.differenceCharacterSet_test()
        return txt
