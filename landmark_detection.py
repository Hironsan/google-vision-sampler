"""
This script uses the Vision API's landmark detection capabilities to find landmark
based on an image's content.

To run the example, install the necessary libraries by running:

    pip install -r requirements.txt

Run the script on an image to get landmark, E.g.:

    ./landmark_detection.py <path-to-image>
"""

import argparse
import os

from utils import Service, encode_image


def main(photo_file):
    """Run a landmark request on a single image"""

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
                    'type': 'LANDMARK_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        response = service.execute(body=body)
        landmark = response['responses'][0]['landmarkAnnotations'][0]['description']
        print('Found landmark: {}'.format(landmark))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect landmark.')
    args = parser.parse_args()
    main(args.image_file)
