"""File Reponsible for placing quotes onto images."""
from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """This class is responsible placing a quote on an image."""

    def __init__(self, output_dir: str):
        """Check for output directory."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate image path."""
        with Image.open(img_path) as img:

            if width is not None:
                width = 500
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text and author is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./font/LilitaOne-Regular.ttf',
                                          size=24)
                draw.text((10, 30), text, font=font, fill='white')
                draw.text((10, 50), author, font=font, fill='white')

        output_file = os.path.join(self.output_dir,
                                   f'.meme_{random.randint(0,10000000)}.jpg')

        img.save(output_file)
        img.close()
        return output_file
