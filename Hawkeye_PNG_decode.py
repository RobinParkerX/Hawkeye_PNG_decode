#!/usr/bin/python3
from PIL import Image
import argparse

KEY_LENGTH = 16

def process(input_file, output_file):
    arr = get_color_values(input_file)
    key = arr[:KEY_LENGTH]
    data = arr[KEY_LENGTH:]

    for i in range(len(data)):
        data[i] ^= key[i % KEY_LENGTH]

    with open(output_file, "wb") as o:
        o.write(data)

def get_color_values(file_name):
    arr = bytearray()
    im = Image.open(file_name)
    w, h = im.size
    for i in range(w):
        for j in range(h):
            r, g, b, t = im.getpixel((i, j))
            if (r, g, b, t) != (0, 0, 0, 0):
                arr.extend([r, g, b])
    return arr

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()
    process(args.input_file, args.output_file)
