def greet(name, message= "How're you doing"):
    print(f"Hello {name}. {message}?")
# function call
greet("Paul" ,"How're you doing")
# You can add a messaage to the second arg, which is printed
# by default if one does not enter message. Making it optional.
def greeting(*names):
    for name in names:
        print(f"Hello {name}")
#function call
greeting("Mary", "Paul", "James", "Cheko")
def factorial(x):
    if x==1:
        return 1
    else:
        return(x* factorial(x-1))

num = 4
print(f"The factorial of {num} is", factorial (num))


