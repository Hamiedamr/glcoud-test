from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()


respone=client.label_detection(image="__path__")
labels=response.label_annotations
print(label)
