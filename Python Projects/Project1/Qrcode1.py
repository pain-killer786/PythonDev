# Make a QR code in python 

import qrcode as qr
img= qr.make("https://sampurnaimagine.com")
img.save("Sampurna_QR.png")