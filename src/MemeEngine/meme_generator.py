"""Represent a class to generate a meme."""

from PIL import Image, ImageDraw, ImageFont
from os import makedirs
from random import randint


class MemeGenerator:
    """
    A class to generate a meme.

    The following responsibilities are defined under this class:

    - Loading of an image from a disk.

    - Transforming the image by resizing to a maximum width of 500px while
      maintaining the input aspect ratio.

    - Adding a caption to the image with a body and author to a random location
      on the image.
    """

    def __init__(self, output_dir: str):
        """
        Create a new `MemeGenerator`.

        Parameters
        ----------
        `output_dir`: str
            output directory to save the generated meme.
        """
        self.output_dir = output_dir
        makedirs(self.output_dir, exist_ok=True)

    def validate_width(self, width: int) -> ValueError:
        """
        Assert whether desired width of the image does not exceed 500px.

        Raise `ValueError` if width greater than 500px.

        Parameters
        ----------
        `width`: int
            width of the image.
        """
        if width > 500:
            raise ValueError('Width of the image cannot exceed 500px.')

    def make_meme(self, img_path: str, text: str,
                  author: str, width: int = 500) -> str:
        """
        Return path of the saved image of the meme after adding caption to it.

        Parameters
        ----------
        `img_path`: str
            path of the original image.

        `text`: str
            quote of the meme.

        `author`: str
            author of the meme.

        `width`: int
            desired width of the image, default = 500px.
        """
        # Opening the image.
        img = Image.open(img_path)

        # Try-except block to handle instances where width > 500px.
        try:
            self.validate_width(width)
        except ValueError as val_err:
            print(val_err)
        else:
            # Resizing the image proportionate to the given width.
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        # Adding the caption to the image.
        caption = f'{text} - {author}'
        font = ImageFont.truetype('./_data/font/Candara.ttf', size=20)

        draw = ImageDraw.Draw(img)
        draw.text(xy=(randint(10, 40),
                      randint(20, 70)),
                  text=caption,
                  font=font,
                  fill='white')

        # Saving the image to the output directory.
        output_path = f'{self.output_dir}/{randint(0, 1000)}.png'

        try:
            img.save(output_path)
        except Exception as e:
            print(e)

        return output_path
