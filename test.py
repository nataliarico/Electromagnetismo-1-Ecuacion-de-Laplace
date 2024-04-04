import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Numérico

a = 0.1
b = 0.1
h = 0.001

potencial = Potencial()


grid= potencial.create_matriz(0, a, 0 ,b, h)
grid= potencial.set_fronteras(7, -7)
grid= potencial.recorrido(epsilon = 10e-4)

x = np.linspace( 0,0.1,100)
y = np.linspace(0, 0.1,100)
X,Y = np.meshgrid(x,y)
Z = potencial.matriz

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)

# Analítico

def v(x, y, V0, N):
  V = 0
  for n in range(1, N):
    Tn = (-2*V0*(-(-1)**n+1))/(n*np.pi)
    Pn= (2*V0*(-(-1)**n+1)*(1+np.cosh(n*np.pi*b)))/(np.sinh(b*n*np.pi)*n*np.pi)
    V += Pn*np.sin(x*n*np.pi)*np.sinh(y*n*np.pi) + Tn*np.sin(x*n*np.pi)*np.cosh(y*n*np.pi)
  return V

a = 0.1
b = 0.1
h = 0.001

potencial = Potencial()
print(v(0.06, 0.04, 7,  100))

grid= potencial.create_matriz(0, a, 0 ,b, h)
grid= potencial.set_fronteras(7, -7)
grid= potencial.recorrido(epsilon = 10e-4)

x = np.linspace( 0,0.1,100)
y = np.linspace(0, 0.1,100)
X,Y = np.meshgrid(x,y)
Z = v(X, Y, -7, 12)

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)
