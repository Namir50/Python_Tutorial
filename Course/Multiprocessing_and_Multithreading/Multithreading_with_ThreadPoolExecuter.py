from concurrent.futures import ThreadPoolExecutor
import time

def numerical_values(numbers):
    time.sleep(1)
    return f"Number : {numbers}"

numbers = [1,2,3,4,5,6,7]

with ThreadPoolExecutor(max_workers = 3) as executor:
    results = executor.map(numerical_values,numbers)

for result in results:
    print(result)