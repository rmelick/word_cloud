
from PIL import Image, ImageFont, ImageDraw
text = u"\U0001f300" #CYCLONE emoji
image = Image.new("RGBA", (100,100), (255,255,255))
font = ImageFont.truetype("/Users/rmelick/Downloads/NotoColorEmoji.ttf", 109, encoding='unic')
draw = ImageDraw.Draw(image)
draw.text((0,0), text, (0,0,0), font=font)
image.save("Test.png")
image.show()