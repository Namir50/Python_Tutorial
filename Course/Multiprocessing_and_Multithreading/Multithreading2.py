import threading
import time

def my_name():
    for i in "Namir":
        time.sleep(2)
        print(f"Letter in my name: {i}")
    
def my_surname():
    for j in "Shah":
        time.sleep(2)
        print(f"Letter in my surname: {j}")

t = time.time() 

t1 = threading.Thread(target=my_name)
t2 = threading.Thread(target=my_surname)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time taken: {time.time()- t}")

