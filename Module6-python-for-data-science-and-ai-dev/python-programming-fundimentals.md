# Python programming fundimentals

## Comparison
```python
6==7    # False
6 != 7  # True

# logic operators
not(True)   # False
not(False)  # True
not(5==5)   # False
not(5==4)   # True

True or False   # True
False or False  # False
1==2 or 2==2    # True

1==1 and 2==2   # True
1==1 and 2==1   # False
```

## Conditions project
[conditions](./projects/conditions-lab.ipynb)

## Conditions and branching
```python
dnd = True

if not dnd:
    send_notification("New message recieved")
```

## Loops
```python
x = range(3)  # [0,1,2]
y = range(1,3) # [1,2]

squares = ["red", "yellow", "green", "purple", "blue"]

for i in range(5):
    squares[i] = "white"

for square in squares:
    print(square)

# Enumerate is good to obtain value and index in the list
for index, square in enumerate(squares):
    print(i,square)

# 0 red
# 1 yellow
# 2 green
# 3 purple
# 4 blue

while(x<4):
    print(x)
    x+=1

# continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# continue
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# 1
# 2
# 4
# 5

# Break
count=0
while count<10:
    count+=1
    if count ==3:
        continue    # skip the rest of this iteration
    if count == 8:
        break   #totaly exit loop for good
    print(count)
```

## Loops project
[loops lab](./projects/loops-lab.ipynb)

## Functions
* built in functions:

```python

random_list=[1,2,4,3]

#len takes in squence (string, list, dictrionary, set)
lenght = len(random_list) # 4

# sum() takes in iterable and returns total of all elements
sum_ratings = sum(random_list)    # 10

# sort a list: 2 ways
# sorted returns new list or tuple
sortled_list = sorted(random_list)    # [1,2,3,4]

#sort changes the list instead of returning one
random_list.sort()  # random_list = [1,2,3,4]
```

* building your own functions
```python

def add(a):
    """
    This is how you document a function
    Make sure to use triple quotes

    you can use the help() command to display info about a fucntion and it will display this text:
        `help(add)`
    """
    return a + 1

add(5)  # 6

def mult(a,b):
    return a*b

print(mult("nic ")) # "nic nic"

# If a function doesnt have a return statment python returns the special `None` object

# mock out a function - pass allows the function to exist with no content
def no_work():
    pass

output = no_work()  # None


# How to input a variable number of elements - collecting arguments
def artists_names(*names):
    for name in names:
        print(name)


# scope - anything defined inside a function has that scope and wont be accessible outside
# global variabels (things defined outside the function or in the global scope) can still be accessed inside the function

# If you do want to define a global variable inside a function, you can use the `global` keyword

def global_keyword_example():
    global value_to_define_as_global
    value_to_define_as_global = 1
    return value_to_define_as_global

global_keyword_example()
print(value_to_define_as_global)

# you dont even have to return it. you can just set it
def set_global_value():
    global my_setting
    my_setting = "Enabled" # Defines the global variable
    
set_global_value()
print(my_setting) # Output: Enabled
```

# Reading - Exploring python functions
```python

# max & min returns max & min value of iterable
l = [1,2,3,4]
highest = max(l)    # 4
lowest = min(l)

# scope
def fn(a):
    a=2 # local scope
a=5
fn(a)
print(a)    # prints 5 still

# global variables
global_variable = "I'm global"

def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable


# If you dont need a value 
def greet(name):
    return "Hello: " + name

for _ in range(3):
    print(greet("nicole"))


# Function to remove an element from a list
# This is a really interesting topic cause did you see the example above when we passed an integer and it didnt change outside the function
# This is because lists are mutabe in python meaning they can change in place but Integers/Strings etc are immutable
# Every time you pass a value to a function in python, you arent passing the actual value but the memory location where that value is stored. Some data types are immuatble like Integers, Strings, Tuples, so if you try to reassign it, it actually just creates a new value with a new memory location so it doesnt affect the original value passed in
# In contrast, since lists, sets, abd ductionaries are mutable, so if you try to change these inside the function, it does update the actual thing you pass
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else: 
        print("element not in data_structure")

remove_element(l,1) # [2,3,4]
```

# Functions project
[functions](./projects/functions.ipynb)

## Exception handling
```python

# try except
try:
    getfile = open("myfile", "r")
    getfile.write("file for exception handling")
except IOError:
    print("unable to open or read data in file")
else:
    print("This runs instead of the except - indicating everything went fine!")
finally:
    file.close()
    print("File has been closed - this always runs")
```

## More on handling exceptions
```python
# Common exceptions in python
result = 10/0   # ZeroDivisionError
num = int("abc") # ValueError

with open("file.txt", "r") as file:
    content = file.read()   # FileNotFoundError

l = [1,2,3]
val = l[10] # IndexError

my_dict = { "name": "nicole"}
age = my_dict.get("age")    # No KeyError using .get()
age = my_dict["age"]    # KeyError

rsult = "hello" + 5 # TypeError

text = "some text"
missing = text.method_not_for_strings() # AttributeError


# Handling an exception
try:
    result = 10/0
except ZeroDivisionError:
    print("Cant divide by 0")

print("Message is outside of try/catch block so will always run")
```

## Exception handling project
[exception handling](./projects/exception-handling.ipynb)

## Objects and classes
```python
# class definition - `class ClassName(object):` - the object is used when you wanna inherit from something - every class is an object so even if you dont write this it still inherits object

class Rectangle(object):

    def __init__(self, colour, height, width):  # constructor
        # self is like a box containing all the data attributes
        self.height = height
        self.colour = colour
        self.width = width

rectangle = Rectangle("blue",2,2)
colour = rectangle.colour
ractangle.colour = "red"    # can change the colour


class Circle(object):
    def __init__(self, colour = "pink", radius = 2):    # we can also add defaults for the params if theyre not passed - this makes them optional
        self.colour = colour
        self.radius = radius
    
    def add_radius(self, r):    # Method
        self.radius = self.radius + r

circle = Circle("green",2)
circle.add_radius(2)
print(circle.radius)    # 4


# dir(name_of_object) is good for getting the attributes and methods associated with a class
dir(circle)
```

# Objects reading
```python

class ClassName:    # notice how we didnt take in object here - it inherits from it by default anyways
    class_attribute = 1 # shared by all instances of class

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method1(self, param1):
        pass    # method logic

obj =  ClassName(1,2)
obj.method1(2)

# to access cllass attributes that are shared by all instances of a class
class_attr = ClassName.class_attribute


# real world example
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:  # see how we access this
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
```

## Classes and objects project
[Classes and objects lab](./projects/classes.ipynb)

# Text analyser project - includes correct count() function usage and more class and object usage
[# Text analyser project - includes correct count() function usage and more class and object usage](./projects/text-analyser-count-function-plus-classes.ipynb)

## Python programming fundimentals cheat sheet
```python
# if-elid-else
score = 85  # Example score
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")

# Output = You got a B.
```