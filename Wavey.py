"""
create a wave of * by gradually increasing the number indents
"""

import time, sys
indent = 0  # How much to indent by
indent_inc = True  # Indent is increasing or not

try:
    while True:  # Main loop
        print(" " * indent, end="")
        print("******")
        time.sleep(.05)  # Time Delay/ Wave speed

        if indent_inc == True:
            # Increase the number of spaces
            indent += 1
            if indent == 10:  # change direction
                indent_inc = False

        if indent_inc == False:
            # Decrease number of spaces
            indent -= 1
            if indent == 0:
                indent_inc = True
except KeyboardInterrupt:
    sys.exit()  # exit system


