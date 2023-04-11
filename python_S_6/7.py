from PIL import Image
frame_img = Image.open("frame.jpg")
Taki_img = Image.open("Taki.jpg")
Taki_img.thumbnail((110, 700))
frame_img.paste(Taki_img, (70, 70))
frame_img.show()
frame_img.save("Taki_in_the_frame.jpg")