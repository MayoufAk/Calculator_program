import os
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y

def cls():
   os.system("cls")

dic = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


def cal():
    f = True
    x = float(input("enter a number :"))
    y = float(input("enter a number :"))
    for i in dic:
        print(i)
    z = input("chose an operation dude ")
    res = dic[z](x, y)
    print(f" {x} {z} {y} = {res}")
    v = res
    while f:
        k = input(f"Type 'y' to continue calculating wit {res}  or 'n' for a new calculation ")
        if k == 'y':
            z = input("enter an opration plz ")
            c = float(input("enter a number "))
            pol = dic[z](res, c)
            print(f" {res} {z} {c} = {pol}")

        if k == 'n':
            f = False
            cls()
            cal()


cal()




