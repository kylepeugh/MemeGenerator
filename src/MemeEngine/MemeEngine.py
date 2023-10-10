

from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def make_meme(self, img_path, text, author, width=500) -> str: #generated image path
        with Image.open(img_path) as img:

            if width is not None:
                width = 500
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)
 
            if text and author is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('.MemeEngine/fonts/LilitaOne-Regular.ttf', size=24)
                draw.text((10, 30), text, font=font, fill='white')
                draw.text((10, 50), author, font=font, fill='white')


            location = img.save(f'./{random.radiant(0,100000)}.jpg')
            return location




