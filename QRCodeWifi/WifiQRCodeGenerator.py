# -*- coding: utf-8 -*-

# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode

# Import Random and String functions
import random, string, datetime

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

senha = randomStringDigits(10)
rede = input("Digite o nome da rede wifi(SSID): ")

"""
if len(senha) < 8:
    print("Senha inválida!")
else:
    print("SSID: " + rede)
    print("SENHA: " + senha)
"""

wifi_code = "WIFI:S:" + rede + ";T:WPA2;P:" + senha + ";;"

print("O QRCode foi gerado a partir deste código " + wifi_code)

qrcode_wifi = pyqrcode.create(wifi_code)

qrcode_wifi.png("wifi_" + rede + ".png", scale = 6)
