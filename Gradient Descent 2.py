# Q2) Write a python code to find the minimum point of the following equation using gradient descent
# f(x) = 2 * (x**2) * cos(x) - 5 * x
# take initial guess from the intervel of (-5,5)


import math
def f(x):
    return 2 * (x**2) * math.cos(x) - 5 * x

def gradient(x):
    return - 2 * (x**2) * math.sin(x) + 4 * x * math.cos(x) - 5

def iterationstop(oldx,newx,epsilon):
    return abs(newx - oldx) < epsilon

def gradient_descent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = oldx - learningrate * gradient(oldx)
        print(iteration,newx,f(newx))
        close = stopiteration(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Minima of the given function is at x = ", newx)
    
gradient_descent(-5,0.01,1000,1e-7)  