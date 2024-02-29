import os
from PIL import Image, ImageFilter

path_name = "D:\iti\personal projects\\automation portfolio\image enhancer\image examples"

for file in os.listdir(path_name):
    if os.path.isfile(os.path.join(path_name, file)):
        with Image.open(os.path.join(path_name, file)) as im:
            blurred = im.filter(ImageFilter.BLUR)
            blurred.save(f"{path_name}\{file}edited.jpg")