# Q3) find the minimum point of the following equation using gradient descent. f(x,y) = 0.26 * (x**2 + y**2) - 0.48 * x*y
# take initial guess from the intervel of (-10,10) for both variables x and y

def f(a,b):
    return 0.26 * (x**2 + y**2) - 0.48 * x*y

def slope(a,b):
    return 0.52 *x - 0.48 * y,0.52 *y - 0.48 * x

def stop(oldx,oldy,newx,newy,epsilon):
    return abs(f(newx,newy) - f(oldx,oldy)) < epsilon

def gd(oldx,oldy,rate,maxiterations,epsilon):
    iteration = 0
    close = False
    while iteration < maxiterations and not close:
        slopex,slopey = slope(oldx,oldy)
        newx = oldx - rate * slopex
        newy = oldy - rate * slopey        
        print(iteration,newx,newy,f(newx,newy))
        close = stop(oldx,oldy,newx,newy,epsilon)
        oldx,oldy = newx,newy
        iteration += 1
        
    print("Minima of the function is at = ",newx,newy)
    
gd(-10,10,0.05,1000,1e-12)
    
