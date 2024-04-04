import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class Potencial:
  def __init__(self):
    #Matriz sobre la que se va a calcular el potencial
    self.matriz= list()

    #Extensión de la matriz
    self.Nx = 0
    self.My = 0

  """Función que crea la matriz e inicializa todos sus valores (incluyendo los internos) arbitrariamente"""
  def create_matriz(self, x_min, a, y_min, b, h):

    self.Nx= int((a - x_min)/h)
    self.My= int((b - y_min)/h)

    for i in range(self.Nx):
      columna= np.random.rand(self.My)
      self.matriz.append(columna)

    self.matriz = np.array(self.matriz)

  """Función que asigna las condiciones de frontera según V0(x,y)"""
  def set_fronteras(self, V0_plus, V0_minus):

    for i in range(self.Nx):
      for j in range(self.My):

        if(i == 0 or i == (self.Nx - 1)):
          self.matriz[i][j] = 0

        elif(j == 0):
          self.matriz[i][j] = V0_minus

        elif(j == self.My - 1):
          self.matriz[i][j] = V0_plus

  #Promedio de los valores vecinos
  def promedio(self, i,j):
    self.matriz[i][j]= ((self.matriz[i+1][j])+(self.matriz[i-1][j])+(self.matriz[i][j+1])+(self.matriz[i][j-1]))/4

  """Se recorre la matriz y se soluciona el potencial usando el método de diferencias finitas con relajación"""
  def recorrido(self, epsilon):
    max_diff = np.inf

    while(max_diff > epsilon):

      #Recorremos los puntos internos de la red y evaluamos el promedio
      max_diff = 0
      for i in range(1, self.Nx - 1):
        for j in range(1, self.My - 1):

          #Anterior al promedio
          old_value = self.matriz[i][j]

          #Calculamos el promedio en este punto
          self.promedio(i, j)

          diff = abs(self.matriz[i][j] - old_value)
          if(diff > max_diff):
            max_diff = diff
