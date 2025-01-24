mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# To insert a list item at a specified index, use the insert() method
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# The remove() method removes the specified item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The clear() method empties the list
# The list still remains, but it has no content

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# You can also loop through the list items by referring to their index number
# Use the range() and len() functions to create a suitable iterable

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# You can loop through the list items by using a while loop
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes

    thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# The condition is like a filter that only accepts the items that evaluate to True

newlist = [x for x in fruits if x != "apple"]

# You can use the range() function to create an iterable

newlist = [x for x in range(10)]

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# You can also customize your own function by using the keyword argument key = function
# The function will return a number that will be used to sort the list (the lowest number first)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
# Make a copy of a list with the copy() method

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Make a copy of a list with the : operator

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join two list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list