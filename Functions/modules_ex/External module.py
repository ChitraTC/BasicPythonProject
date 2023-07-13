import pyqrcode
path="P:\collage-5-05\IMG_20220712_071239.jpg"
s="Nakshatra Degish"
url=pyqrcode.create(path)
url.svg("DegishNakshatraqrcode.svg",scale=8)



