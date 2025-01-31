#Task1

def togramm(ounces):
    return(ounces*28.3495231)

#Task 2

def toC(F):
    return F*(5 / 9) * (F - 32)

#Task3

def solve(numheads, numlegs):
    rabs = (numlegs - 2*numheads)//2
    chicks = numheads - rabs
    return rabs, chicks

#Task 4

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

def filter_prime(m):
    filtered = []
    for i in m:
        if(prime(i)):
            filtered.append(i)

    return filtered

#Task 5

def perm(str):
    if len(str) == 1:
        return str
    lst = []
    for i in range(len(str)):
        for j in perm(str[:i]+str[i+1:]):
            lst.append(str[i]+j)
    return lst
    

    



#Task 6

def inverse(lst):
    str = lst.split()
    print (*list(str[::-1]))

#Task 7

def tri(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
     
    return False

#Task 8

def spy(lst):
    cntzr = 0
    for i in lst:
        if i == 0:
            cntzr+=1
        elif i == 7 and cntzr == 2:
            return True
    return False



#Task 9 

def vol(Rad):
    return (4/3)*3.14*Rad**3

#Task 10
def uniquelist(st):
    st.sort()
    unique_st = []
    for i in st:
        if i not in unique_st:
            unique_st.append(i)
    return unique_st

#Task 11

def pol(str):
    rev = str[::-1]
    if rev == str:
        return True
    return False

#Task 12

def his(lst):
    for i in lst:
        print('*'*i)

#Task 13
import random

def ugaday():
    n = random.randint(1,21)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    m = int(input())
    cnt = 1
    while m != n:
        if m > n:
            print("Your guess is too high.\nTake a guess")
        else:
            print("Your guess is too low.\nTake a guess")
        m = int(input())
        cnt += 1
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")