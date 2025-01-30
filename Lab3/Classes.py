import math

class Up():
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Input smth: ")
    
    def printString(self):
        print(self.s.upper())


s = Up()

s.getString()
s.printString()


class Shape:
    def __init__(self, a = 0, b = 0):
        self.length = a
        self.width = b
    
    def area(self):
        print(self.length * self.width)

class Square:
    def __init__(self, a):
        self.size = a
    
    def area(self):
        print(self.size ** 2)


shape = Shape()
shape.area()

square = Square(4)
square.area()


class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        print(self.length*self.width)


rectangle = Rectangle(2,5)
rectangle.area()


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)
    
    def move(self, gox, goy):
        self.x = gox
        self.y = goy

    def dist(self, secpoint):
        print(math.sqrt((secpoint.x - self.x)**2 + (secpoint.y - self.y)**2))


point1 = Points(2,3)
point2 = Points(9,7)

point1.show()
point1.move(1,3)
point1.show()

point1.dist(point2)


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, cashin):
        self.balance += cashin
        print(f"You have {self.balance}$")

    def withdrawal(self, cashout):
        if self.balance >= cashout:
            self.balance -= cashout
            print(f"You have {self.balance}$")
        else: 
            print(" Withdrawals may not exceed the available balance")

account = Account("Beka", 0)
account.deposit(1000000)
account.withdrawal(999999)
account.withdrawal(2)

def prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%2 == 0:
            return False
    return True

lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19,20]

prlst = list(filter(lambda nondef: prime(nondef), lst))

print(prlst)
