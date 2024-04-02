#::::: Default Library :::::
import time
import sys

#::::: Slow Print :::::
def slowprint(s):
    "A Function to print a sentence word for word."
    for c in s +"\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)