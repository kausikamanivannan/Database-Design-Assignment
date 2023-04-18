import time
import random

'''
    Website: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/#
    I used code from this website. It contains a fibonacci function that returns the nth term (which depends on the randomly generated n value).
    This code checks if the value is a negative (which is invalid), then if the input is zero or one (which returns zero or one respectively). 
    All other values will get the fibonacci value.
'''

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
'''
    Website: https://docs.python.org/3/library/random.html
    This website has the details of the randint function, which generates a random number within the requierments.

    Website: https://stackoverflow.com/questions/24836901/value-modifying-decorator-on-recursive-python-function
    This website has code that measures the execution time of a peice of code. The difference between the start_time variable and long_time variable is the total execution time.
'''

n = random.randint(15, 35)

start_time = time.time()
result = fibonacci(n)
end_time = time.time()
total_time = end_time - start_time

print(f"fib({n})={result}")
print(f"fib({n}) took {total_time} seconds")