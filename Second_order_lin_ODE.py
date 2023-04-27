import matplotlib.pyplot as plt
import math


#2nd order linear ODE solver
#aD^2x + bDx + cx = f(x)

dt = 0.01
a = 1
b = 2
c = 1
L = 100
N = int(L/dt)
x0 = 1
Dx0 = 1


t = [dt*i for i in range(0,N)]
f = [math.sin(0.01*i*dt) for i in range(0,N)]

#D^2x  2Dx +x = f
x = [x0]
Dx = [Dx0]
D2x = []
D2x.append(f[0]-b*Dx0-c*x0)


for i in range(0,N-1):
    D2x.append((f[i]-c*x[i]-b*Dx[i])/a)
    Dx.append(Dx[i] + D2x[i+1]*dt)
    x.append(x[i]+Dx[i+1]*dt)





plt.plot(t,x)
plt.show()