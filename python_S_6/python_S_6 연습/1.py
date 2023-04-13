from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
f = open("male_lion", 'r')
canvas_size = (1000, 1000)
lion_size = (900, 900)
data = f.readlines()
Frame_img = Image.open("frame.jpg")
Lion_img = Image.open("Lion.jpg")
Lion_rsz = Lion_img.resize(lion_size)
Frame_rsz = Frame_img.resize(canvas_size)
Frame_rsz.paste(Lion_rsz, (50, 50, 950, 950))
msg = 'Animal : Male lion\nFamily : Felidae\nBinomial name : Panthera leo\nHabitat : Africa\nHead-and-body length : 170-298cm\nTail length : 90-105cm\nWeight : 150-250kg'
draw = ImageDraw.Draw(Frame_rsz)
draw.text((50, 50), msg, (0, 0, 255))
Frame_rsz.show()
Frame_img.save("Male_Lion.jpg")