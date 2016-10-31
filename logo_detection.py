"""
This script uses the Vision API's logo detection capabilities to find logo
based on an image's content.

To run the example, install the necessary libraries by running:

    pip install -r requirements.txt

Run the script on an image to get logo, E.g.:

    ./logo_detection.py <path-to-image>
"""

import argparse
import os

from utils import Service, encode_image


def main(photo_file):
    """Run a logo request on a single image"""

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
                    'type': 'LOGO_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        response = service.execute(body=body)
        logo = response['responses'][0]['logoAnnotations'][0]['description']
        print('Found logo: {}'.format(logo))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect logo.')
    args = parser.parse_args()
    main(args.image_file)
