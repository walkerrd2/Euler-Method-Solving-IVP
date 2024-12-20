import numpy as np
import matplotlib.pyplot as plt

def davis_euler(f,a,b,alpha,n):
    h = (b-a)/n
    t = np.linspace(a, b, n)
    w = np.zeros(n)

    w[0] = alpha
    for i in range(0,n-1):
        w[i+1] = w[i]+(h*f(t[i],w[i]))
    return t, w


#def f(t,y):
    #return y-(t**2)+1

#a=0
#b=2
#alpha=0.5
#h=0.2 #or use h=(b-a)/n
#n=10 #or use n=int((b-a)/h)
#tvals, wvals = davis_euler(f,a,b,alpha,n)

#print(tvals, wvals) #compare to Table 5.1, page 268

#plt.plot(tvals,wvals,'c^',label="Approx Solution") #a graph of the approximate solution w

#def y(t):
    #return (t+1)**2 -0.5*np.exp(t) #this is the exact solution to the above IVP
    
#yvals=y(tvals)
#plt.plot(tvals, yvals,'r-',label="Exact Solution") # graph of the exact solution y(t)
#plt.xlabel('x values')
#plt.ylabel('y values')
#plt.title("Euler's Method")
#plt.legend()
#plt.grid()
#plt.show()

def f(t,y):
    return np.e**(t)*np.cos(t)

a=0
b=5
alpha=1
h=0.01#or use h=(b-a)/n
n=int((b-a)/h) #or use n=int((b-a)/h)
tvals, wvals = davis_euler(f,a,b,alpha,n)

print(tvals, wvals) #compare to Table 5.1, page 268

plt.plot(tvals,wvals,'r-',label="Approx Solution") #a graph of the approximate solution w

#def y(t):
    #return (t**2)+((1/3)*np.e**(-5*t)) #this is the exact solution to the above IVP
    
#yvals=y(tvals)
#plt.plot(tvals, yvals,'r-',label="Exact Solution") # graph of the exact solution y(t)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title("Euler's Method")
plt.legend()
plt.grid()
plt.show()


