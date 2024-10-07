import time


def hinh_1():
    for y in range(3, -4, -1):
        for x in range(-3, 4):
            if x > 0 > y or x < 0 < y:
                print(" ", end=" ")
            elif x >= 0 and y >= 0:
                if x + y <= 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif x <= 0 and y <= 0:
                if x <= y:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print("")

def hinh_2():
    for y in range(3, -4, -1):
        for x in range(-3, 4):
            if x > 0 > y or x < 0 < y:
                print(" ", end=" ")
            elif x >= 0 and y >= 0:
                if x + y <= 3:
                    if x==y==1:
                        print(" ", end=" ")
                        continue
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            elif x <= 0 and y <= 0:
                if x <= y:
                    if x==-2 and y==-1:
                        print(" ", end=" ")
                        continue
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print("")

def hinh_4():
    for y in range(3, -4, -1):
        for x in range(-3, 4):
            if y > 0 > x:
                print(" ", end=" ")
            elif x > 0 and y > 0:
                if x == y:
                    for z in range(x + 1):
                        if x == 2 and y == 2 and z == 1:
                            print(' ', end=' ')
                            continue
                        print("*", end=" ")
            elif x <= 0 and y <= 0:
                if x == y:
                    for j in range(3 + y):
                        print(" ", end=" ")
                    for z in range(-y + 1):
                        if x == -2 and y == -2 and z == 1:
                            print(' ', end=' ')
                            continue
                        print("*", end=" ")
        print("")

def hinh_3():
    for y in range(3, -4, -1):
        for x in range(-3, 4):
            if y>0>x:
                print(" ", end=" ")
            elif x > 0 and y > 0:
                if x==y:
                    for z in range(x+1):
                        print("*", end=" ")
            elif x <= 0 and y <= 0:
                if x==y:
                    for j in range(3+y):
                        print(" ", end=" ")
                    for z in range(-y+1):
                        print("*", end=" ")

        print("")


hinh_1()
time.sleep(5)
hinh_2()
time.sleep(5)
hinh_3()
time.sleep(5)
hinh_4()
time.sleep(5)