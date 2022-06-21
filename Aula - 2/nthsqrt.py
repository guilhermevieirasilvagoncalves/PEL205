import cv2
import numpy as np

imagem = cv2.imread("lena.jpg",0)

col = imagem.shape[1]
lin = imagem.shape[0]

imagemR = np.zeros((lin,col))

for y in range(1, lin):
    for x in range(1, col):
        r = imagem[y,x] 
        imagemR[y,x] = r ** np.sqrt(1.1)

cv2.imshow("imagem Resultado",imagemR/255)
cv2.waitKey(0)
cv2.destroyAllWindows()
