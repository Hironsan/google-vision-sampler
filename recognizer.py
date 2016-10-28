#!/usr/bin/python
#coding:utf-8
import base64
import json
import os
from requests import Request, Session
import requests

# !/usr/bin/python
# coding:utf-8

import os
import sys
import base64
import json
import requests

# APIのURL
api_url = 'https://vision.googleapis.com/v1/images:annotate?key='

# APIキー
api_key = os.environ.get('VISION_API', None)

# リクエスト用のデータ作成
with open(sys.argv[1], 'rb') as image:
    base64_image = base64.b64encode(image.read()).decode()
    """
    data = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'FACE_DETECTION',
                'maxResults': 100,
            }]

        }]
    }
    """

    data = {
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

    # リクエスト送信
    header = {'Content-Type': 'application/json'}
    response = requests.post(api_url + api_key, json.dumps(data), header)

    # 分析結果の取得
    if response.status_code == 200:
        # print response.text
        json_response = json.loads(response.text)
        # 顔認識の結果が含まれていれば切り出す
        print(json_response)
        import pprint
        pprint.pprint(json_response)
        if json_response['responses'][0].has_key('faceAnnotations'):
            # 認識できた顔の数だけループ
            for i, face in enumerate(json_response['responses'][0]['faceAnnotations']):
                # 顔画像位置
                vertices = [(v.get('x', 0.0), v.get('y', 0.0)) for v in face['fdBoundingPoly']['vertices']]
                # print vertices
                # 顔画像の切り出し
                #src = cv2.imread(sys.argv[1])
                #dst = src[vertices[0][1]:vertices[2][1], vertices[0][0]:vertices[2][0]]
                # 顔画像の出力パスを作成
                #root, ext = os.path.splitext(sys.argv[1])
                #face_image_path = root + '_face' + str(i) + ext
                # 顔画像の出力
                #cv2.imwrite(face_image_path, dst)
        else:
            print('顔が認識されませんでした')
    else:
        print('Http response error')

