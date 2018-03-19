# -*- coding: utf-8 -*-
#!/usr/bin/env python
from misc.Output import execute_MAIN_STRING
from DOCS.FamilyInfo import *


def main():
    txt = ""
    ###TESTS:
    setup = Setup(commands, mainArg)
    txt += setup.getTxt()
    MAIN_STRING = txt
    execute_MAIN_STRING(MAIN_STRING)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2 and sys.argv[-1][0] != "-":
        commands = (sys.argv)[1:-1]
        mainArg = (sys.argv)[-1]
    else:
        commands = (sys.argv)[1:]
        mainArg = None
    # mainArg = "diff-masters"
    main()
