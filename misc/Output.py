import time
def output(str):
    print(str)
    time.sleep(.03)

def execute_MAIN_STRING(MAIN_STRING):
    lines = MAIN_STRING.split("\n")
    for i in range(len(lines)):
        line = lines[i]

        if i+1 < len(lines):
            if line == lines[i+1] and line == "```":
                continue
            output(line)
            # print(line)
