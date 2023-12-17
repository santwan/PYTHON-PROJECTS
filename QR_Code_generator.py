import qrcode 

img = qrcode.make("https://www.youtube.com/watch?v=onrFahjosQY")

qrcode.image.pil.PilImage #type(img)

img.save("yotube.png")

