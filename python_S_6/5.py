from PIL import Image
from PIL import ImageDraw
circle_area = [(25, 50), (450, 850)]
Taki_img = Image.open("Taki.jpg")
draw_img = ImageDraw.Draw(Taki_img)
draw_img.ellipse(circle_area, outline = "yellow")
Taki_img.show()
Taki_img.save("Yellow_circled_Taki.jpg")