
def jsonify_decorator(function):    
    def modifyOutput():
        return {"output": function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return "hello world"

@jsonify_decorator  # this takes in the function defined below it
def add():
    num1 = input("enter a number")
    num2 = input("Enter another number")
    return int(num1) + int(num2)

print(hello())
print(add())