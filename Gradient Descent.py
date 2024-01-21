# Q1. Find the x_new upto 4 iterations using gradient descent ( By hand) formulae for minimization, take learning rate = 0.01
# 1) (x+5)^2, x_guess = 5
# 2) 5x^3 + 2x^2 − 3x, x_guess = 0 3) x^2 - 4, x_guess
# = 2 for maximization,
# 1) 3 + 14x − 5x^2, x_guess = 1 2) -x^2 + 5, x_guess = 2
# 3) 5x^3 + 2x^2 − 3x, x_guess = 0

import math
def f(x):
    return (x+5)^2

def gradient(x):
    return 2x + 10

def iterationstop(oldx,newx,epsilon):
    return abs(newx - oldx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = oldx - learningrate * gradient(oldx)
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Minima of the given function is at x = ", newx)
    
gradientdescent(5,0.01,1000,1e-7)  

-------------------------------------------------------------

import math
def f(x):
    return 5x^3 + 2x^2 − 3x

def gradient(x):
    return 15x^2 + 4x

def iterationstop(oldx,newx,epsilon):
    return abs(newx - oldx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = oldx - learningrate * gradient(oldx)
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Minima of the given function is at x = ", newx)
    
gradientdescent(0,0.01,1000,1e-7)  

-------------------------------------------------------------

import math
def f(x):
    return x^2 - 4

def gradient(x):
    return 2x

def iterationstop(oldx,newx,epsilon):
    return abs(newx - oldx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = oldx - learningrate * gradient(oldx)
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Minima of the given function is at x = ", newx)
    
gradientdescent(2,0.01,1000,1e-7)  

-------------------------------------------------------------

import math
def f(x):
    return 3 + 14x − 5x^2

def gradient(x):
    return 14 - 10x

def iterationstop(oldx,newx,epsilon):
    return abs(oldx - newx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = learningrate * gradient(oldx) - oldx
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Maxima of the given function is at x = ", newx)
    
gradientdescent(1,0.01,1000,1e-7)  

-------------------------------------------------------------

import math
def f(x):
    return -x^2 + 5

def gradient(x):
    return -2x

def iterationstop(oldx,newx,epsilon):
    return abs(oldx - newx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = learningrate * gradient(oldx) - oldx
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Maxima of the given function is at x = ", newx)
    
gradientdescent(2,0.01,1000,1e-7)  

-------------------------------------------------------------

import math
def f(x):
    return 5x^3 + 2x^2 − 3x

def gradient(x):
    return 15x^2 + 4x - 3

def iterationstop(oldx,newx,epsilon):
    return abs(oldx - newx) < epsilon

def gradientdescent(oldx,learningrate,maxiteration,epsilon):
    iteration = 0
    close = False
    while iteration < maxiteration and not close:
        newx = learningrate * gradient(oldx) - oldx
        print(iteration,newx,f(newx))
        close = iterationstop(oldx,newx,epsilon)
        oldx = newx
        iteration = iteration + 1
        
    print("Maxima of the given function is at x = ", newx)
    
gradientdescent(0,0.01,1000,1e-7)  