from concurrent.futures import ProcessPoolExecutor
import time


def factorial(number):
    result = 1
    time.sleep(1)
    for i in range(1,number+1):
        result = result * i    
    print(result)

number = [10,235,5435]

with ProcessPoolExecutor(max_workers=3) as executor:
    results = executor.map(factorial,number)

for result in results:
    print(result)