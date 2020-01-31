from PIL import Image, ImageFont, ImageDraw

import numpy

scale = 1
default_char = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft我爱Python'


def image_conversion(import_img, export_img=None, input_char='', pix_distance=''):
    """
    @params
        import_img: the path of the imported image
        export_img: the path of the exported image
        input_char: the customized content of char painting, if the param is None, use the default value
        pix_distance: density of the char painting
    """
    # read in an img
    image = Image.open(import_img)
    # get image pixel
    image_pixel = image.load()
    # get image height and width
    image_height = image.height
    image_width = image.width

    canvas_array = numpy.ndarray((image_height * scale, image_width * scale, 3), numpy.uint8)
    canvas_array[:, :, :] = 255
    new_image = Image.fromarray(canvas_array)
    img_draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype('simsun.ttc', 10)

    if input_char == '':
        char_list = list(default_char)
    else:
        char_list = list(input_char)

    if pix_distance == '清晰':
        pix_distance = 3
    elif pix_distance == '一般':
        pix_distance = 4
    elif pix_distance == '字符':
        pix_distance = 5

    pix_count = 0
    table_len = len(char_list)
    for y in range(image_height):
        for x in range(image_width):
            if x % pix_distance == 0 and y % pix_distance == 0:
                img_draw.text((x * scale, y * scale), char_list[pix_count % table_len], image_pixel[x, y], font)
                pix_count += 1

    if export_img is not None:
        new_image.save(export_img)

    return False
