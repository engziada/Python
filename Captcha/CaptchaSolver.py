from PIL import Image

im = Image.open("pp1.png")
im = im.convert("P")
im2 = Image.new("P", im.size, 255)

im = im.convert("P")

temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        temp[pix] = pix
        if pix == 220 or pix == 227:
            # these are the numbers to get_
            im2.putpixel((y, x), 0)
print(pix)
im2.save("output.gif")
