import cv2 as cv
import numpy as np 
import mahotas
# Contar os lados do dados que estão para cima 
imagem_colorida = cv.imread("Imagens/img02.png")

def escrever(imagem,texto,cor=(255,0,0):
    fonte = cv.FONT_HERSHEY_SIMPLEX 
    cv.putText(imagem,texto,(10,20),fonte,0.5, cor, 0, cv.LINE_AA) 

imagem = cv.cvtoColor(imagem_colorida, cv.COLOR_BRG2GRAY)
desfoque = cv.blur(imagem,(7,7)) 
# Binarização da imagem, resultando em pixel branco e preto 

