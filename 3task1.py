import sys

def cmd():
    cd = "command line"
    sys.stdout = print(cd)

cmd()
