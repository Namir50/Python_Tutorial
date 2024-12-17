
import time 
import threading

name = input("Enter your name: ")
phone  = input("Enter your phone number: ")

def name_function():
    for i in name:
        time.sleep(2)
        print(f"Letter in your name: {i}")

def phone_function():
    for j in phone:
        time.sleep(2)
        print(f"Digit in your phone number: {j}")

t = time.time()

t1 = threading.Thread(target = name_function)
t2 = threading.Thread(target = phone_function)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time taken: {time.time() - t}")

# phone  = input("Enter your phone number: ")

# def name_function():
#     for i in name:
#         time.sleep(2)
#         print(f"Letter in your name: {i}")

# def phone_function():
#     for j in phone:
#         time.sleep(2)
#         print(f"Digit in your phone number: {j}")

# t = time.time()

# t1 = threading.Thread(target = name)
# t2 = threading.Thread(target = phone)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"Time taken: {time.time() - t}")