#1
import functools
def multiply_list(vremyas):
    return functools.reduce(lambda x, y: x * y, vremyas)

nums = [1, 2, 3, 4, 5]
result = multiply_list(nums)
print("Product of vremyas:", result)


#2
str = "Hello World"
appr = 0
lowr = 0
for i in str:
    if i.isupper():
        appr += 1
    elif i.islower and i != " ":
        lowr += 1

print(appr, lowr)


#3
def is_palindrome(strr):
    strr = strr.replace(" ", "").lower()
    if str == str[::-1]:
        print(f'"{strr}" is a palindrome.')
        return
    else:
        print(f'"{strr}" is not a palindrome.')
        return

str1 = "level"
is_palindrome(str1)

str2 = "bye"
is_palindrome(str2)

#4
import time

chislo = 25100
zaderzhka = 2123

time.sleep(zaderzhka / 1000)  

res = chislo ** 0.5

print(f"Square root of {chislo} after {zaderzhka} milliseconds is {res}")


#5
def isTrue(tup):
    return all(tup)

tup1 = (True, True, True)
tup2 = (True, False, True)

print(isTrue(tup1))
print(isTrue(tup2))