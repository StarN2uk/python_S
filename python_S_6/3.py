from PIL import Image
from PIL import ImageDraw
canvas_size = (200, 200)
rect_area = [(0, 0), (100, 100)]
line_cor = [(0, 200), (200, 0)]
circle_area = [(100, 100), (200, 200)]
new_img = Image.new("RGB", canvas_size, "orange")
draw_imgs = ImageDraw.Draw(new_img)
draw_imgs.rectangle(rect_area, fill = "red", outline = "yellow")
draw_imgs.line(line_cor, fill = "blue", width = 4)
draw_imgs.ellipse(circle_area, fill = "green", outline = "red")
new_img.show()
new_img.save("imagedraw.jpg")