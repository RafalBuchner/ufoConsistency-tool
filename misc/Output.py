# -*- coding: utf-8 -*-
import time
import sys
"""
    It products output in terminal, which lines are printed with small delay
"""
def output(string):
    if sys.version_info < (3,1,1):
        print(u"{}".format(string.encode('utf-8')))
    else:
        print(string)
    time.sleep(.02)

def execute_MAIN_STRING(MAIN_STRING):
    lines = MAIN_STRING.split("\n")
    if len(lines) > 1:
        for i in range(len(lines)):
            line = lines[i]

            if i+1 < len(lines):
                if line == lines[i+1] and line == "```":
                    continue
                output(line)
    else:
        output(lines[0])
