# Make a QR code in python 

import qrcode as qr
img= qr.make("https://www.facebook.com/the.whiteknight786")
img.save("Facebook_QR.png")