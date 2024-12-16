import threading
import time

def my_name():
    for i in "Namir":
        time.sleep(2)
        print(f"Letter in my name:{i}")
    
def my_surname():
    time.sleep(2)
    for j in "Shah":
        print(f"Letter in my surname{j}")

t = time.time()

