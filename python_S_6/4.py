from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
Taki_img = Image.open("Taki.jpg")
c3coding_img = Image.open("c3coding_rt.jpg")
c3coding_img.thumbnail((120, 120))
draw = ImageDraw.Draw(Taki_img)
stx, sty = (150, 285)
c3x, c3y = c3coding_img.size
msg = "The               is"
msg2 = "the best!"
#mfont = ImageFont.truetype("FRADM.TTF", 40)
#m2font = ImageFont.truetype("DROADW.TTF", 52)
draw.text((70, 280), msg, (255, 255, 0), align = "Left")
draw.text((70, 330), msg2, (255, 0, 0), align = "Left")
Taki_img.paste(c3coding_img, (stx, sty, stx+c3x, sty+c3y))
Taki_img.show()
Taki_img.save("c3Taki.jpg")