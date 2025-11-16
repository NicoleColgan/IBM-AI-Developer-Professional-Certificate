# Python basics

## Expessions and variabales lab
* integer dission is rounded DOWN to the nearest integer
[expressions variables and bimdas](./projects/Expressions_Variables.ipynb)

## Strings
* each character in a string can be indexed by a number
* Escape sequences are strings that map be difficult to imput. `\` proceeds an escape sequence. you you want to place a literal backslash in your srting. use a double backslace or place an r infront of the string

```python
name= "nicole"
firstLetter = name[0]

# can also use negative indexing in strings
lastLetter = name[-1]

# you can treat the string as a sequence and perform sequence operations
fullName = "nicole colgan"
firstName = fullName[0:6]   #note, the first index is included but the last isnt
lastName = fullName[7:13]   #see can we go to the last index

# you can skip the last index if you want to go to the end or from the start to a certain index you can skip first
lastName = fullName[7:]
firstName = fullName[:6]

print(firstName)    #nicole
print(lastName) #colgan

# you can also indicate a step
everySecondLetter = name[::2]   #ioe

# slicing - return every second value up to index 4
sliced = name[0:5:2]    #io

# length of string
len(name)   #6

# replicate a string
name*3  #nicolenicolenicole

# you cannot change the value in a string but you can create a new one
name[0] = "k"   # X - this is not aloud

escapeSequence = "hello\n"
stringWithBackslash = "tea\\coffee"
otherOptionToIncludeBackslash = r"tea\coffee"
```
### String methods
* since strings are sequences, they have sequence methods then normal string methods
* When we apply a method to a string we get a new string

```python
name="nicole"
upper_name = name.upper()   #NICOLE - notice how it returns a value and doesnt just modify name

# replace a part of string with a new string (it creates a new string tho. it doesnt actually replace it)
fullName = "nicole colgan"
firstName = fullName.replace(" colgan","")

# find substrings - returns starting index
starting_index_fullName = fullName.find("colgan")   #7
starting_index_fullName = fullName.find("col")    # 7 - another way to do this since we only get the first index anyways
starting_index_fullName = fullName.find("xyz")  # -1 : represents not found

# split a string at a specified character and produce a list 
# usage: string.split(seperator, maxsplit)
# seperator = delimiter to split string: default = whitespace
# maxsplit = max number of splits to perform: default = no max

```

## Format strings in python
* 3 different ways to format strings

```python
name="nicole"
age=25
print(f"my name is {name} and my age is {age}")

# another way to do this is with str.format()
print(f"my name is {} and my age is {}".format(name,age))

# another way - % operator
print(f"my name is %s and my age is %d" % (name, age))

# can also use f strings to evaluate equations
print(f"2+2={2+2}")
```
* raw strings are important too because in certain cases you want to treat strings as string literals to get the correct result
```python
path = "C:/nicole/project"  
print(path) # the "/n" in the string will be escaped so it will move half the string to the next line which we dont want

# raw string (prefix with r) which isnt escaped
raw_string = r"C:/nicole/project"   # prints correctly
print(raw_string)   # C:/nicole/project
```
