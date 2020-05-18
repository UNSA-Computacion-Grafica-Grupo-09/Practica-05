import cv2
import numpy as np
from matplotlib import pyplot as plt


#obtenemos la imagen en escala de grises y tambbien loutilizamos para guardar el resultado de la imagen
imagen_gray = cv2.imread('exp_6.jpg', cv2.IMREAD_GRAYSCALE)
imagen_resultado = cv2.imread('exp_6.jpg', cv2.IMREAD_GRAYSCALE)

alto,ancho = imagen_gray.shape #Calculamos la dimencion de la imagen
print(alto,ancho)

cv2.imshow('Original',imagen_gray) #Convertimos a grises

hist = cv2.calcHist([imagen_gray], [0], None, [256], [0, 256])


#Inicializamos lo valores de c para hacer nuestras pruebas
#c=10
c=70
#c=50
#c=70
#c=100



#Utilizremos operador punto:

for i in range(alto):
    for j in range(ancho):
        #raiz=c*(np.sqrt(imagen_gray[i][j]))#Aplicamos nuestro operador raiz
        raiz=c*(np.log10(imagen_gray[i][j]))
        
        if(raiz<0):# Si el resultado del pixel es un valor menor que 0 
            imagen_resultado[i][j]=0#Se le asignara 0
        elif(raiz>255):# Si el resultado del pixel es un valor menor que 255
            imagen_resultado[i][j]=255#Se le asignara 0
        else:
            imagen_resultado[i][j]=raiz# Si los valores estan entre el rango de [0,255] se guardan sin mofiicacion


#Calculamos histogramas para ver su funcionamiento

hisR = cv2.calcHist([imagen_resultado], [0], None, [256], [0, 256])


cv2.imshow('Resultado',imagen_resultado) #mostramos el resultado

cv2.imwrite('res.jpg',imagen_resultado) #guardamos el resultado
plt.plot(hist, color='blue' ) 
plt.plot(hisR, color='red' )


plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()
