import cv2

imagem = cv2.imread("lena.jpg",0)

col = imagem.shape[1]
lin = imagem.shape[0]
m = 80
for y in range(1, lin):
    for x in range(1, col):
        r = imagem[y,x]
        if r > m:
            s = 255
        else:
            s = 0
        imagem[y,x] = s

cv2.imshow("imagem Resultado",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


