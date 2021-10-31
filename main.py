from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:\Users\user\Documents\QR-Code\myqrcode.png')

result = decode(img)

print(result)