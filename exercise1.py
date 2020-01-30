# 1
def namesake(name):
    print(name)

# 2
def namecap(name):
    n = name.upper()
    print(n)

# 3
listcomp = [ x.upper() for x in "smogtether"]

# 4
def number():
    num = 0
    while True:
        num += 1
        if num%2 == 0:
            yield num
        elif num%2 != 0:
            yield num


