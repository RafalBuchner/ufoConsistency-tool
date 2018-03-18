from misc.Output import output

def fatal(expression, string):
    """
        Error for command prompt
    """
    if not expression:  # FATAL ERROR???
        # from sys import exit
        # exit("\n [**FATAL ERROR**]> {}\n\n".format(string))
        output("\n [**FATAL ERROR**]> {}\n".format(string))

def consider(string, MAIN_STRING):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """

    MAIN_STRING += "\n [**CONSIDER**]> {}\n\n".format(string)
    return MAIN_STRING



def warning(expression, string, MAIN_STRING, countError=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """
    if countError != None:
        if not expression:  # WARNING ERROR???
            MAIN_STRING += "\n [**WARNING**]> {} > #{}\n\n".format(string, countError)
    else:
        if not expression:  # WARNING ERROR???
            MAIN_STRING += "\n [**WARNING**]> {}\n\n".format(string)
    return MAIN_STRING
