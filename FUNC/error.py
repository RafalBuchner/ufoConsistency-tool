from misc.Output import output

def fatal(expression, string):
    """
        Error for command prompt
    """
    if not expression:  # FATAL ERROR???
        # from sys import exit
        # exit("\n [**FATAL ERROR**]> {}\n\n".format(string))
        output("\n [**FATAL ERROR**]> {}\n".format(string))

def consider(string, font=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """

    txt = "\n [**CONSIDER**]> {}\n\n".format(string)

    if font:
        txt += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
            font.path.split("/")[-1])
    return txt



def warning(expression, string, font=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """
    if not expression:  # WARNING ERROR???
        txt = "\n [**WARNING**]> {}\n\n".format(string)

    if not expression:  # WARNING ERROR???
        txt = "\n [**WARNING**]> {}\n\n".format(string)

    if font:
        txt += "\\\\\\\\\\\\\\\ *FILE NAME: {}*\n".format(
            font.path.split("/")[-1])
    return txt
