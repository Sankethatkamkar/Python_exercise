class aircraft:
    x=4
    y=5
    acc=2

    def __init__(a, x, y):
        a.x = x
        a.y = y

a = aircraft(0,0)

def moveup(y):
    y+=1

    return y

def moveleft(x):
    x-=1
    return x

def moveright(x):
    x+=1
    return x

def movedown(y):
    y-=1
    return y

y = a.y
x = a.x


for i in range(2):
    x = moveleft(x)


for i in range(4):
    y= moveup(y)


for i in range(2):
    y = movedown(y)


for i in range(4):
    x = moveright(x)

print("Coordinates in x-plane:",x)
print("Coordinates in y-plane:",y)
