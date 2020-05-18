# -*- coding: utf-8 -*-
"""
Created on Tue May 12 07:34:57 2020

@author: MILAGROS PC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


imagen = cv2.imread('log_6.jpg')
imagen_resultado = cv2.imread('log_6.jpg')
imagen_gray = cv2.imread('log_6.jpg', cv2.IMREAD_GRAYSCALE)
imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)

#------------------------------------------------------------------------
#Implementacion de algoritmo de Operador exponencial 

# Inicializamos los valores 5 10 20  21  

b = 3
c = 50

alto, ancho = imagen_gray.shape


for x in range(alto):
    for y in range(ancho):
        resultado = c * (np.power(b,imagen_gray[x][y]) - 1)
        if resultado > 255:
            imagen_resultado[x][y] = 255
        else:
            imagen_resultado[x][y] = c * (np.power(b,imagen_gray[x][y]) - 1)
        
                 

#------------------------------------------------------------------------
#Implementacion de algoritmo de Raise to the power operator 

#Inicializamos los valores 1 1.2 1.9 2 2.5 para c cundo r = 0.8

# r = 0.8
r = 1
# c = 4
c = 3
# #valores de c 1 1.2 0.5 0.8 3 cuando r = 1
alto, ancho = imagen_gray.shape


for x in range(alto):
    for y in range(ancho):
        resultado = (c * (np.power(imagen_gray[x][y] , r)))
        if resultado > 255:
            imagen_resultado[x][y] = 255
        elif resultado < 0:
            imagen_resultado[x][y] = 0
        else:
            imagen_resultado[x][y] = (c * (np.power(imagen_gray[x][y] , r)))   
#-------------------------------------------------------------------------

plt.imshow(imagen_resultado)
plt.savefig('Imagen_resultado_3.jpg', bbox_inches='tight')