"""
Multithreading
When to use Multithreading: 
  I/O bound tasks: tasks that spend more time wwwaiting for I/O operations(e.g.: file operation, network requests)
  Concurrent operations: when you want to improve the throughput of your application by performing multiple operations concurrently"""
  
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number:{i}")

def print_letters():
    for letter in "abcde":
        print(f"Letter:{letter}")

t = time.time()
print_numbers()
print_letters()
print(f"Time take: {time.time() - t}")