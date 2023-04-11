from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
circle_area = [(0, 20), (250, 150)]
circle2_area = [(70, 70), (100, 100)]
circle3_area = [(100, 100), (100, 100)]
Taki_img = Image.open("Taki.jpg")
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120, 120))
draw = ImageDraw.Draw(Taki_img)
stx, sty = (50, 50)
c3x, c3y = c3coding_img.size
msg = "The                         is"
msg2 = "the best!"
draw_img = ImageDraw.Draw(Taki_img)
draw_img.ellipse(circle_area, outline = "black")
draw_img.ellipse(circle2_area, fill = "black", outline = "black")
draw_img.ellipse(circle3_area, fill = "black", outline = "black")
draw.text((20, 50), msg, (255, 255, 0), align = "Left")
draw.text((20, 100), msg2, (255, 0, 0), align = "Left")
Taki_img.paste(c3coding_img, (stx, sty, stx+c3x, sty+c3y))
Taki_img.show()
Taki_img.save("Thinking_Taki.jpg")