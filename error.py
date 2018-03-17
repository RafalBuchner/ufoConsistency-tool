def fatal(expression, string):
    """
        Error for command prompt
    """
    if not expression:  # FATAL ERROR???
        sys.exit(f"[FATAL ERROR]//> {string}")

def warning(expression, string, countError=None):
    """
        Error for command prompt
        Count=If count is needed, then you have to change countError to something else than None:
        assign countError to variable put before loop, which equals 1.
        After the warning you have to implement the incrementation of this variable
    """
    if countError != None:
        if not expression:  # WARNING ERROR???
            print(f"[WARNING]//> {string} > {countError}")
    else:
        if not expression:  # WARNING ERROR???
            print(f"[WARNING]//> {string}")
