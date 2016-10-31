# -*- coding: utf-8 -*-
import base64

import requests


class Service(object):

    def __init__(self, service_name, version, access_token):
        self.url = 'https://{}.googleapis.com/{}/images:annotate?key={}'.format(service_name, version, access_token)

    def execute(self, body):
        header = {'Content-Type': 'application/json'}
        response = requests.post(self.url, headers=header, json=body)
        return response.json()


def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content).decode()
