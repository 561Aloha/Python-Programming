#homework 1 final answers
""" QUESTION ONE"""

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

try:
    a = float(input("Enter the value of 'a': "))
    b = float(input("Enter the value of 'b': "))
    c = float(input("Enter the value of 'c': "))
    if a == 0: # ensuring a cant be zero, 
        print("A cannot be 0")
    else: 
        quad = b**2 - 4*a*c
        if quad < 0:
            print('No real solutions')
            x_opt = -b / (2*a) #centering the
        elif quad == 0:     #compute solutions
            x = -b / (2*a)
            print('There is one solution:', x)
        else:
            x1 = (-b + sqrt(quad)) / (2*a)
            x2 = (-b - sqrt(quad)) / (2*a)
            print('There are two solutions:', x1, x2)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")

#use linspace to evenly distribute, x_opt only gets factered in if quad <0,
x_values = np.linspace(x_opt - 10, x_opt + 10, 150)
y_values = quadratic_function(x_values, a, b, c)

plt.plot(x_values, y_values, label='Quadratic Function')
            
# Plot the roots
plt.scatter([x1, x2], [0, 0], color='blue', label='Roots')

# Set x label, y label, and title
plt.xlabel("x")
plt.ylabel("y")
plt.title('Problem 1')
plt.legend()
plt.show()        


"""
QUESTION TWO

With the formula a^ + b^2 = c^2 we rearranged using algebra to 
isolate each letter. We use We have a empty list that will hold any pairs.
Since n <= to c and 0<a we use these conditions to set the start:stop of the range

while on the inside, we iterate through each number 1-10 (in our example) and 
carry out the algebratic formala. Once we find the pairs, we add them to the tuples list"""
def find_Pythagorean(n):
    tuples = []
    c, i = 0, 2 #pattern matching

    while c < n:
        for j in range(1, i):
            a = i **2 - j**2
            b = 2 * i * j
            c = i **2  + j**2

            if c > n:
                break

            tuples.append((a, b, c))
            tuples.append((b, a, c)) #for including all possible triples
        i += 1

    return tuples


find_Pythagorean(10)

""" Question 3"""
def find_dup_str(s, n):
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        for j in range(i + 1, len(s) - n + 1):
            if s[j:j + n] == substring:
                print('The Duplicates ',substring)
                return True  # Return as soon as a duplicate is found
    return False


s = 'abcddcbcd'
n = 2
find_dup_str(s,n)
print()

def find_max_dup(s):
    n = 0
    for length in range(1, len(s)):
        if find_dup_str(s, length):
            n = length
        else:
            break  # Stop if no more duplicates are found
    return n #the resule

s = 'abcddcbcd'
result = find_max_dup(s)
print("Maximum duplicate length:", result)

"""Question 4"""
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    step = (xmax - xmin) / (ns - 1)

    xs = [xmin + i * step for i in range(ns)]  # Generate ns evenly spaced points
    ys = [eval(fun_str.replace('x', str(x))) for x in xs]  # Evaluate fun_str for each x

    # Plot the function
    plt.plot(xs, ys)

    # Set x label, y label, and title
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)

    # Show the plot
    plt.show()


fun_str = input("Enter function with variable x: ") #2 * math.sin(2*math.pi * x)
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ns = int(input("Enter the number of samples (ns): "))


plot_function(fun_str, (xmin, xmax), ns)
