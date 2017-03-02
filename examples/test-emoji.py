#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
import unicodedata
import re
import sys

frog = u'🐸'
print ("frog is")
print(frog)

fileLines = open("simple-emoji.txt").readlines()
print("file lines are")
print(fileLines)
print("each line is")
for emojiString in fileLines:
    print(emojiString)

text = "".join(fileLines)
regexp = r"\S[\S']+"
flags = (re.UNICODE if sys.version < '3' and type(text) is unicode
                 else 0)
print("combined text is")
print(text)

words = re.findall(regexp, text, flags)
print("words are")
print(words)