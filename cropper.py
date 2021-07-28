import os

from PIL import Image, ImageChops


def trim(im, margin):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        bbox = (bbox[0] - margin, bbox[1] - margin, bbox[2] + margin, bbox[3] + margin)
        return im.crop(bbox)


def process(path: str, filename: str, margin: int):
    im = Image.open(path + filename)
    out_path = path.replace('inbox', 'outbox')
    os.makedirs(out_path, 777, True)
    trim(im, margin).save(out_path + filename)

    return out_path + filename

if __name__ == "__main__":
    process('0007.jpg', margin=20)
