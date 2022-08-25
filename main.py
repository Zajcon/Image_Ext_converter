from PIL import Image
import os

def empty_callback(value):
    pass
files = os.listdir()
images = [file for file in files if file.endswith(('webp'))]

class Error(Exception):

    pass
def convert_image(image_path, image_type):
    im = Image.open(image_path)
    im = im.convert('RGB')
    image_name = image_path.split('.')[0]
    print(f"This is the image name: {image_name}")

    if image_type == 'webp':
        im.save(f"{image_name}.jpg", 'jpeg')
    else:
        raise Error
for image in images:
    if image.endswith('webp'):
        convert_image(image, image_type='webp')
    else:
        raise Error

string_matches = ['webp']
for file in os.listdir():
    if any(x in file for x in string_matches):
        os.remove(file)

#if __name__ == '__main__':
#    main()
