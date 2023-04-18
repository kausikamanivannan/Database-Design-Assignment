import numpy as np

'''
    Website: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    The rand function creates an array of 10 random floats

    Website: https://www.geeksforgeeks.org/compute-the-mean-standard-deviation-and-variance-of-a-given-numpy-array/
    This website shows how to use functions to calculate the mean, median, and standard deviation.
'''
random_array = np.random.rand(10)

mean = np.mean(random_array)
median = np.median(random_array)
std = np.std(random_array)

print("Random Numbers: ", random_array)
print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", std)
