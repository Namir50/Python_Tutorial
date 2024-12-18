from concurrent.futures import ProcessPoolExecutor
import time

def numerical_values(numbers):
    time.sleep(1)  #will executefaster if we dont use this function
    return f"Numbers: {numbers}"

numbers = [132,453,543,123,543,566]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(numerical_values,numbers)
        
    for result in results:
        print(result)