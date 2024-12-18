#Processes that run in parallel
#Used for tasks that are heavy on CPU(e.g.: mathematical computations, data processing)
#Uses multiple cores of the CPU to speed up the process            

import multiprocessing
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i**2}")
        
def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i**3}")
        
if __name__ == "__main__":  #just creating an entry point
    p1 = multiprocessing.Process(target = square)
    p2 = multiprocessing.Process(target = cube)
    
    t = time.time()
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Time taken is : {time.time()-t}")
    