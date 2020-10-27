def dw(x,x1,h):
    r= x-x1
    R = abs(r)/h
    if R<=1:
        return -12*R*(1-R)**2/h*r/abs(r)*5/(4*h)
    else:
        return 0
import math
import matplotlib.pyplot as plt
xmin =-5
xmax =5
n = 1000
dx = (xmax-xmin)/n
h=3*dx
x=[]
y=[]
y1=[]
#i=50
Sum =0
for i in range(10,n-10):
    #fx=math.sin(i)
    j=0
    Sum=0
    xi =xmin+i*dx
    for j in range(n):
        xj =xmin+j*dx
        #if abs((i-j)/n)<=h:
        if i!=j:
            #Sum+=math.sin(xj)*dw(xi,xj,h)*dx
            #Sum+=(math.log(xj))*dw(xi,xj,h)*dx
            Sum+=(xj**2-xj+1)*dw(xi,xj,h)*dx
    x.append(xi)
    y.append(xi**2-xi+1)
    y1.append(Sum)
plt.plot(x,y)
plt.plot(x,y1)
plt.legend()
plt.show()
