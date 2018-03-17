class TableStringMD(object):
    """
    Creates ascii string table prepared for MarkDownFormatting.
    In order to use it you should provide
    it with the list of rows (which are also lists).

    Positioning of the table:
    (R describes index number of the row,
    while L describes index number of the
    cell in the row, it can
    be precieved as index of the line )

      |    R0 |    R1 |    R2 |    R3 |  add1 |  add2
-------------------------------------------------------|
   L0 | R0-L0 | R1-L0 | R2-L0 | R3-L0 |       |
   L1 | R0-L1 | R1-L1 | R2-L1 | R3-L1 |       |
   L2 | R0-L2 | R1-L2 | R2-L2 | R3-L2 |       |
   L3 | R0-L3 | R1-L3 | R2-L3 | R3-L3 |       |
 add1 |       |       |       |       |       |
 add2 |       |       |       |       |       |

    What's so more you can add description
    of the line and description of the row (as list of strings).
    The indexing of lines and rows starts in top-left corner of
    the table, so first row description will be above farest left row,
    and first line description will appear above highest line.

    Example:
    lineInfo = ["L0","L1","L2","L3"]
    rowInfo = ["R0","R1","R2","R3"]
    print TableStr([x for x in rows],lineInfo=lineInfo,rowInfo=rowInfo).create()

    """
    def __init__(self, rows, lineInfo = [], rowInfo = []):
        self.lineInfo = lineInfo
        self.rowInfo = rowInfo
        self.rows = rows
        self._initDescriptions()

    def _initDescriptions(self):
        if self.lineInfo != []:
            self.rows.insert(0, self.lineInfo)

        if self.rowInfo != []:
            if self.lineInfo != []:
                self.rowInfo.insert(0,"")

            if len(self.rows) < len(self.rowInfo):
                numOfEmptyRows = len(self.rowInfo)-len(self.rows)
                for i in range(numOfEmptyRows):
                    self.rows.append([""])

            for i in range(len(self.rows)):
                self.rows[i].insert(0,self.rowInfo[i])

    def getCellWidth(self):
        """ returns width (in characters) of the single cell:
            self.getLenOfBiggestCell() + 2, where 3 is for the bar and spaces between next cell"""
        return self._getLenOfBiggestCell() + 2

    def _getLenOfBiggestCell(self):
        """ Returns number of characters used for the text in the biggest cell in the table:
            It helps to calculate dimentions of the single cell"""
        newTable = []
        for row in self.rows:
            newRow = []
            for cell in row:
                newCell = len(str(cell))
                newRow.append(newCell)
            newTable.append(newRow)
        return max([max (row) for row in newTable])

    def getTableStringMD(self):
        """
            returns table as string
        """
        biggestLen = self._getLenOfBiggestCell()
        largest =  max(self.rows, key=lambda coll: len(coll)) # row with the biggest number of lines
        numberOfLines = len(largest)
        lineIndex = 0
        tableStr = ""

        for lineIndex in range(numberOfLines):
            line = ""
            for row in self.rows:
                if (len(row)-1) >= lineIndex:
                    cell = str(row[lineIndex])
                    currLen = len(cell)

                    spaces = (biggestLen - currLen) * " "
                    line += spaces + cell + " | "
                else:
                    currLen = 0
                    spaces = (biggestLen - currLen) * " "
                    line += spaces +              " | "

            tableStr += ("|"+line+"\n")
            if lineIndex == 0:
                tableStr += "|"+(len(line)-2)*"-"+"|\n"


        return tableStr
    def getTableListMD(self):
       table_str = self.getTableStringMD()
       return table_str.split("\n")

# rows = [
#     ["R0-L0","R0-L1","R0-L2","R0-L3"],
#     ["R1-L0","R1-L1","R1-L2","R1-L3"],
#     ["R2-L0","R2-L1","R2-L2","R2-L3"],
#     ["R3-L0","R3-L1","R3-L2","R3-L3"],
# ]
# lineInfo = ["L0","L1","L2","L3","add1","add2"]
# rowInfo = ["R0","R1","R2","R3","add1","add2"]
#
# table = TableStringMD([x for x in rows],lineInfo=lineInfo,rowInfo=rowInfo)
# print(table.getTableStringMD())
# print(table.getCellWidth() * 2 * " ", "Text shifted by 2 cells widths")
