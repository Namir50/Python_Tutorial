import time 
import threading

x = input("Enter your name: ")
y  = int(input("Enter your phone number: "))

def x_function():
    for i in x:
        time.sleep(2)
        print(f"Letter in your name: ")

def y_function():
    for j in y:
        time.sleep(2)
        print(f"Digit in your phone number: ")

