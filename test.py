import tweepy
from PIL import Image, ImageDraw, ImageFont
import textwrap


image2 = Image.open('bolsonaro3.jpg')
draw = ImageDraw.Draw(image2)
font = ImageFont.truetype('arial.ttf', size=14)
message = ("oiiii")
textwrapped1 = textwrap.wrap(message, width=20)
color = 'rgb(0, 0, 0)' # black color
draw.multiline_text((70, 35),'\n'.join(textwrapped1), font=font, fill="#aa0000")
image2.save('3bolso.jpg')