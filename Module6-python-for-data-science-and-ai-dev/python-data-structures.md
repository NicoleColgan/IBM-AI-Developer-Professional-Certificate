# Python data structures

## tuples & lists

### Tuples
* tuples are ordered sequence
* tuples are immutible

```python
ratings = (10,9,8,4)    # tuple

t1 = ("string", 1.0, 1, True)   # can have many diff types

val1 = t1[0]    # accessing tuple

last_val = t1[-1]   # can use negative indexing

combined_tuple = t1 + rating    # ("string", 1.0, 1, True, 10,9,8,4)

sliced_tuple = ratings[0:3] # (10,9,8)

nested_tuple = ((1,2), 3, ("nic", "col"), (4, (5, 6)))

accesing_nested_tuple = nestes_tuple[0][1]   # get index one of element 0 (1,2) = 2

# We can even go further into the indexing
first_name_initial = nested_tuple[2][0][0]  # n

double_nested = nested_tuple[3][1][0]   # 5
```

### Lists
* lists are like tuples but theyre mutable
* can contain mix of types too
* List aliasing - if you assign one variable name to another list, they reference the same list in memory so changing one changes the other too

```python

l1 = ["Michael Jackson", 10, [1,2], ('A', 1)]   # can have any type

l1_el1 = l1[0]  # accessing works the same way as tuples
t1 = l1[-1] 
slice_l1 = l1[0:2]

l2 = [0,1]
l3 = l1 + l2

# Since lists are mutible, we can change them
l2.extend(["pop", 10])  # extend with new list
l2.append(1)    # only adds one element
l2[0] = "new val"   # l2 = ["new val", 1, "pop", 10, 1]
del(l2[-1]) # l2 = ["new val", 1, "pop", 10]

# Convert string to a list using split
"Nicole Colgan".split() # default is space - ["Nicole", "Colgan"]
"Nicole,Colgan".split(",") # can give delimiter - ["Nicole", "Colgan"]

# List aliasing - if you assign a variable to be another list, they reference the same list in memory so if you change one it will be reflected in the other (alias)
l4= [0,1]
l5=l4
l4[0] = "changed"
print(l5)   # ["changed", 1]

# If you dont want this behaviour, you can clone a list like this
clone = l4  # now you can change the clone and l4 wont be affected
```

* To get help on lists
```python
help(["list", "t"])
```

## Lists project
[lists](./projects/lists-lab.ipynb)

# Tuples project
[tuples](./projects/tuples-lab.ipynb)

## More on tuples & lists
```python
t1 = (1,4,3)
print(sorted(t1))   # (1,3,4)
print(len(t1))

print("disco".find("s"))

# Lists
# Create copy of list
l1 = [1,2,3]
l2 = l1.copy()

# count number of occurences of specific elemen in a list
number_of_1s = l1.count(1)  #1

# insert an element in an index - insert(index, item)
my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)  # [1,2, 6 , 4,5]

#pop can be used to delte an element at a specified index - or if none is provided, it removes the last element and returns it
first_el = my_list.pop(0)    #1
print(my_list)  # [2,6,4,5]
last_el = my_list.pop() # 5
print(my_list)  # [2,6,4]

# remove() removes first occurance of specified value
another_list = [1,1,2,3,1]
another_list.remove(1)  # another_list = [1,2,3,1]

# reverse a list
another_list.reverse()   # [1,3,2,1]

# sort() sorts a list in ascending order. If you want to sort in descending you can pass `reverse=True` as an arg
another_list.sort() # [1,1,2,3]
another_list.sort(reverse=True) # [3,2,1,1]
```

### Tuples
```python
# count how many times a spcified element appears in a list
t1 = (1,2,1,3)
print(t1.count(1))  # 2

# find first index of a value - if not found, returns ValueError
print(t1.index(1))  # 0

# sum() adds all elements provided all ints or floats
print(sum(t1))  # 7

# min() & max()
print(min(t1))  # 1
print(max(t1))  # 3

# len() number of elements in tuple
print(len(t1))  # 4
```

## Dictionaries
* kv pairs
* keys have to be immutible and unique
* values can be mutible & duplicates

```python
d1 = {
    "k1": 1,
    "k2": "2",
    "k3": [1,2,3],
    "k4": (444),
    ("k5"): 5   # tuples are immutable so they can be keys
    }

v1 = d1["k1"]   # Accessing a value

d1["k6"] = 6    # Adding new value to dictionary

del(d1["k6"])   # delete an entry

# Check if a value is in the dictionary
print("k1" in d1)   # prints True

# See all the keys in a dictionary
d1.keys()

# See all values
d1.values()
```

## Dictionaries project
[dictionaries](./projects/dictionaries-lab.ipynb)

## Sets
* Another collection
* Theyre not orderes so you never know where a value will  be
* sets only have unique elements
* If duplicates are entered into the set, they will be filtered out
```python
s1 = { "v1", "v2", "v3", "v1", "v1" }   # s1 = { "v1", "v2", "v3" }

# you can convert a list to a set
l1 = [1,1,2,3,4]
s2 = set(l1)    # converts to set and removed duplicates

s2.add(5)   # s2 = {1,2,3,4,5}
s2.add(5)   # s2 = {1,2,3,4,5} - nothing happens since 5 is already in the set
s2.remove(5)

# check is element in set
print(1 in s2)  #True

# find intersection of 2 sets
s3 = {4,5,6,7}
intersection = s2 & s3  # {4,5}

# Union of 2 sets
s2.union(s3)

# check if se is a subset
s4 = {1,2}
s4.issubset(s2) #True

# find items in one set that arent in another set
s2.difference(s4)   # {3,4,5}

# A superset is a set that contains all the elemnts in another set - it can contain more too
s2.issuperset(s4)   #True since s4 contains 1 and two and both elements are in s2
s4.issuperset(s2)   # False - missing {3,4,5}
```

### Sets project
[sets](./projects/sets-lab.ipynb)

## Dictionaries and sets cheat sheet
```python

del dict_name[key]  # raises key error if it doesnt exist

# update a key and value in a dict
dict_name.update({key: value})

# Delete everything in a dictionary
dict_name.clear()

# create copy of a dictionary - different objects in memory so changing one wont affect the other
new_dict = old_dict.copy()

# get alll kv pairs in dict - creates a list of tuples where each tuple has 2 vals, key and val
items_list = list(dict_name.items())

## Sets

set_name.clear()
set_name.copy()
new_set = set()
newer_set = {1,2}

# use discard to delte elements from set. ignores if element isnt found
set_name.discard(element)

# pop removes arbitrary element in a set but since they dont have order, it just pops any element - raises keyError if element not found in set
removed_element = set_name.pop()

# remove removes by key and returns keyError is  not in set
set_name.remove(e2)

# update() adds elements from another iterable to aset - mainaining uniqueness
set_name.update([1,2])
```
