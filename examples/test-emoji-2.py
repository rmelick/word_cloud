# -*- coding: utf-8 -*-
import io
from os import path
from PIL import Image, ImageFont, ImageDraw
d = path.dirname(__file__)

# Read the whole text.
textPath = path.join(d, 'simple-emoji.txt')
oldText = open(textPath).read()
text2 = u'🌀'
text = io.open(textPath).read()
#text = "test" #CYCLONE emoji
#text = u"test \U0001f300" #CYCLONE emoji
image = Image.new("RGBA", (500,500), (255,255,255))
font = ImageFont.truetype("/home/rmelick/Downloads/fonts/Symbola.ttf", 109, encoding = "unic")
#font = ImageFont.truetype("/home/rmelick/Downloads/fonts/NotoColorEmoji.ttf", 109, encoding = "unic")
#font = ImageFont.truetype("/home/rmelick/Downloads/fonts/NotoSans-Regular.ttf", 109, encoding = "unic")
draw = ImageDraw.Draw(image)
draw.text((0,0), text, (0,0,0), font=font)
image.save("Test.png")
image.show()