import matplotlib.pyplot as plt
dt=0.01
t = 0
k=10
x1=3
x2=5
x3=10
v1 = 0
v2=0
v3=0
T=[]
X1=[]
X2=[]
X3=[]
m1=1
m2=2
m3=3
dx1=0
dx2=0
dx3=0
while t <=20:
    
    a1 = -k*(x1-(x2-5))/m1
    v1 = v1+a1*dt
    dx1 =v1*dt
    x1 = x1 + dx1
    X1.append(x1)

    a2 = (x1-(x2-5)-((x2-5)-(x3-10)))*k/m2
    v2 = v2+a2*dt
    dx2 = v2*dt
    x2 = x2+dx2
    X2.append(x2)
    
    a3 =((x2-5)-(x3-10))*k/m3
    v3 = v3+a3*dt
    dx3=v3*dt
    x3 = x3+dx3
    X3.append(x3)
    
    T.append(t)
    t+=dt

plt.plot(T,X1)
plt.plot(T,X2)
plt.plot(T,X3)
plt.show( )
