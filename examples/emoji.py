#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""
import io
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = io.open('/home/rmelick/Downloads/chat.txt').read()

# Generate a word cloud image
wordcloud = WordCloud(font_path="/home/rmelick/Downloads/fonts/Symbola.ttf",  width=1200, height=600).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path="/home/rmelick/Downloads/fonts/Symbola.ttf", max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
