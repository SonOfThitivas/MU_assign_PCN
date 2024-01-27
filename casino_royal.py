#Assignment 1 : Experimental Analysis of Algorithm Complexity (final)
#Phimchanok Laonok
#ID: 6687035
#Sec: 1

#Task1
#Write a function for constant time complexity (𝑂(1)).
def constant_time_function():
    print("This function has constant time complexity.")
constant_time_function()
#Write a function for linear time complexity (0(n)).
def linear_time_function(n):
    for i in range(n):
        print(i)
linear_time_function(5)
#Write a function for quadratic time complexity (0 (n)).
def quadratic_time_function(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
quadratic_time_function(3)
#Write a function for logarithmic-linear time complexity (O (n log n)).
import math
def log_linear_time_function(n):
    for i in range(1, n + 1):
        print(i, int(math.log2(i)))
log_linear_time_function(3)
#Task2 Measure Execution Time 
#For each algorithm, measure the time it takes to execute with different input sizes. Use arange of input sizes (e.g., from 1 to 500, increasing by 50 for each measurement).
import time
def linear_time_function(n):
   
    for i in range(n):
        pass  

input_sizes = list(range(1, 29999))

for size in input_sizes:
    start_time = time.time()
    linear_time_function(size)
    end_time = time.time()
    
    execution_time = end_time - start_time
    print(f"Input Size: {size}, Execution Time: {execution_time} seconds")


#Task3 Plotting and Analysis 
#Use a plotting library  to plot the execution times against theinput sizes for each algorithm.
import time
import matplotlib.pyplot as plt

def constant_time_function():
    pass

def linear_time_function(n):
    for i in range(n):
        pass

def quadratic_time_function(n):
    for i in range(n):
        for j in range(n):
            pass

def log_linear_time_function(n):
    for i in range(1, n + 1):
        pass

input_sizes = list(range(1, 501, 50))

constant_times = []
linear_times = []
quadratic_times = []
log_linear_times = []

for size in input_sizes:
    start_time = time.time()
    constant_time_function()
    end_time = time.time()
    constant_times.append(end_time - start_time)

    start_time = time.time()
    linear_time_function(size)
    end_time = time.time()
    linear_times.append(end_time - start_time)

    start_time = time.time()
    quadratic_time_function(size)
    end_time = time.time()
    quadratic_times.append(end_time - start_time)

    start_time = time.time()
    log_linear_time_function(size)
    end_time = time.time()
    log_linear_times.append(end_time - start_time)

plt.figure(figsize=(10, 6))

plt.plot(input_sizes, constant_times, label='Constant Time')
plt.plot(input_sizes, linear_times, label='Linear Time')
plt.plot(input_sizes, quadratic_times, label='Quadratic Time')
plt.plot(input_sizes, log_linear_times, label='Log-Linear Time')

plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Algorithmic Time Complexity Analysis')
plt.legend()

plt.show()


#Analyze the plots and write a summary of your observations regarding how the execution time scales with the input size for each complexity.