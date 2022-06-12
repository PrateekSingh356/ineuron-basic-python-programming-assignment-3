#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
def check(x):
    if x<0:
        print("negative number.")
    elif x==0:
        print("zero number.")
    else:
        print("number positive.")
check(55)