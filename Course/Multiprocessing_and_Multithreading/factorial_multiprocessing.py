from concurrent.futures import ProcessPoolExecutor
import time

def factorial(number):
    result = 1
    time.sleep(1)
    for i in range(1,number+1):
        result = result * i    
    return result

number = [10,143,23]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(factorial,number)

    for result in results:
        print(result)