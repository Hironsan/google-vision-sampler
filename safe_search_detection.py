"""
This script uses the Vision API's safe search capabilities to find inappropriate content
based on an image's content.

To run the example, install the necessary libraries by running:

    pip install -r requirements.txt

Run the script on an image to detect inappropriate content, E.g.:

    ./safe_search_detection.py <path-to-image>
"""

import argparse
import os

from utils import Service, encode_image


def main(photo_file):
    """Run a safe search request on a single image"""

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
                    'type': 'SAFE_SEARCH_DETECTION',
                    'maxResults': 1,
                }]

            }]
        }
        response = service.execute(body=body)
        level = response['responses'][0]['safeSearchAnnotations']
        print('Found level: {}'.format(level))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to detect inappropriate content.')
    args = parser.parse_args()
    main(args.image_file)
