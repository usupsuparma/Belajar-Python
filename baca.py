from PIL import Image

im = Image.open("b.jpg")
width, heigt = im.size
print(width,heigt)