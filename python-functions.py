# def func_name():
#     print("My name is Vincent Kimanthi.")

# func_name()

#Passing of arguments and parameters in Python
#lName = "Kimanthi"
#def my_func(fName, lName, age):
    #print(fName + " it's awesome")
#     print(f"{fName} {lName} is {age} years old.")

# my_func("Vincent", "Kimanthi", 20)

#Function that collect user inputs
def myUser_func(fName):
    return "Hello " + fName
greet = myUser_func(input("Enter your name: "))
print(greet)
