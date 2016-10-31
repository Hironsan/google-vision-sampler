# google-vision-sampler
Code examples for Google Vision API written in Python.

## Description
Example codes has following features:

* Face Detection
* Landmark Detection
* Logo Detection
* Label Detection
* Text Detection
* Safe Search Detection

## Requirement

* Python 3.x
* API Token(Vision API)

## Usage
Set Google Vision API Token to environment variables.

```
$ export VISION_API=xxxxx
```


### Face Detection
![face](https://github.com/Hironsan/google-vision-sampler/blob/master/images/face.jpg)

### Label Detection
![label](https://github.com/Hironsan/google-vision-sampler/blob/master/images/label.jpg)

### Landmark Detection
![landmark](https://github.com/Hironsan/google-vision-sampler/blob/master/images/landmark.jpg)

### Logo Detection
![logo](https://github.com/Hironsan/google-vision-sampler/blob/master/images/logo.jpg)

### Text Detection
![text](https://github.com/Hironsan/google-vision-sampler/blob/master/images/text.png)


## Install

```
$ pip install -r requirements.txt
```

## Image Sizing
To enable accurate image detection within the Google Cloud Vision API, images should generally be a minimum of 640 x 480 pixels (about 300k pixels). Full details for different types of Vision API Feature requests are shown below:

| Vision API Feature | Recommended Size | Notes |
|---|---|---|
| FACE_DETECTION | 1600 x 1200 | Distance between eyes is most important |
| LANDMARK_DETECTION | 640 x 480 |   |
| LOGO_DETECTION | 640 x 480 |   |
| LABEL_DETECTION | 640 x 480 |   |
| TEXT_DETECTION | 1024 x 768 | OCR requires more resolution to detect characters |
| SAFE_SEARCH_DETECTION | 640 x 480 |   |

## Licence

[MIT](https://github.com/Hironsan/google-vision-sampler/blob/master/LICENSE)

## Author

[Hironsan](https://github.com/Hironsan)