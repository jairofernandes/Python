#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import os

img02 = cv2.imread('selo.png')

caminho = "./EMPRESA_ENMAC"
saida = "./ENMAC"

for nomearquivo in os.listdir(caminho):
    print(nomearquivo)
    if nomearquivo == 'Thumbs.db':
        continue
    else:
        path = os.path.join(caminho, nomearquivo)
        camapnha = os.path.join(saida, nomearquivo)
        img01 = cv2.imread(path)
        imv = cv2.vconcat( [img01, img02] )
        cv2.imwrite(camapnha, imv)