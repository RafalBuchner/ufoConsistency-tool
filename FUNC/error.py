# -*- coding: utf-8 -*-

def fatal(expression, string):
    """
        Error for command prompt
    """
    if not expression:  # FATAL ERROR???
        # from sys import exit
        # exit("\n [**FATAL ERROR**]> {}\n\n".format(string))
        print(u"\n [**FATAL ERROR**]> {}\n".format(string))

def consider(string, font=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """

    txt = u"\n [**CONSIDER**]> {}\n\n".format(string)

    if font:
        txt += u"\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
            font.path.split("/")[-1])
    return txt



def warning(expression, string, font=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """

    txt = ""

    if not expression:  # WARNING ERROR???
        txt = u"\n [**WARNING**]> {}\n\n".format(string)

        if font != None:
            txt += u"\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
                font.path.split("/")[-1])
    return txt
