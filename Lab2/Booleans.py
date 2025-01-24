a = 23
b = 96

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(10 > 9)
print(10 == 9)
print(10 < 9)


# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))


# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")