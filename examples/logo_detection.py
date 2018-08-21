import argparse
import io

from google.cloud import vision
from google.cloud.vision import types


def main(image_file):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.logo_detection(image=image)
    annotations = response.logo_annotations
    for annotation in annotations:
        print(annotation.description)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
