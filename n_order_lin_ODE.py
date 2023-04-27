import matplotlib.pyplot as plt
import math


#2nd order linear ODE solver
#aD^2x + bDx + cx = f(x)

dt = 0.01
n = int(input("Enter the order of equation: "))
L = 100
N = int(L/dt)
init = []
c = []

for i in range(0,n):
    print("{0} {1:d} {2}".format("Enter ",i,"th derivative of x at t=0"))
    a = float(input("Enter: "))
    init.append(a)


for i in range(0,n+1):
    print("{0} {1:d} {2}".format("Enter the constant of ",i,"th derivative of x"))
    a = float(input("Enter: "))
    c.append(a)



t = [dt*i for i in range(0,N)]
f = [0 for i in range(0,N)]

a = f[0]
for i in range(0,n):
    a = a - c[i]*init[i]
init.append(a/c[n])
#D^2x  2Dx +x = f
x = []

for i in range (0,n+1):
    x.append([init[i]])



for i in range(0,N-1):
    a = f[i]
    for j in range(1,n+1):
        a = a - c[n-j]*x[n-j][i]
    x[n].append(a)
    for j in range(1,n+1):
        x[n-j].append(x[n-j][i]+dt*x[n+1-j][i+1])


plt.plot(t,x[0])
plt.show()