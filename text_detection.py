"""
This script uses the Vision API's text detection capabilities to find a text
based on an image's content.

To run the example, install the necessary libraries by running:

    pip install -r requirements.txt

Run the script on an image to get text, E.g.:

    ./text_detection.py <path-to-image>
"""

import argparse
import os

from utils import Service, encode_image


def main(photo_file):
    """Run a text detection request on a single image"""

    access_token = os.environ.get('VISION_API')
    service = Service('vision', 'v1', access_token=access_token)

    with open(photo_file, 'rb') as image:
        base64_image = encode_image(image)
        body = {
            'requests': [{
                'image': {
                    'content': base64_image,
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        response = service.execute(body=body)
        text = response['responses'][0]['textAnnotations'][0]['description']
        print('Found text: {}'.format(text))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect text.')
    args = parser.parse_args()
    main(args.image_file)
