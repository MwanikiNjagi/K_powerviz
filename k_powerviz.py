import numpy as np
def f(x):
    return(10**x)
x = int(input())#Value of Power you want

#Prints values in float format rather than decimal format
def format_float(num):
    return np.format_float_positional(num, trim='-')
    
for x in range(-x, x+1):
    print(format_float(f(x)))