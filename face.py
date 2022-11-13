from base64 import encode
from email.mime import base
import cv2
import face_recognition
import sys
import base64
from PIL import Image
import io
import numpy as np


def base64toImage(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

def analyze_user(base64_string, face2):
    
    baseimg = base64toImage(base64_string)


    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    sampleimg = base64toImage(face2)

    try:
        samplefacetest = face_recognition.face_locations(sampleimg)[0]
        encodesamplefacetest = face_recognition.face_encodings(sampleimg)[0]
    except IndexError as e:
        print(e)
        sys.exit()

    result = face_recognition.compare_faces([encodemyface], encodesamplefacetest)
    resultstring = str(result)
    # print(resultstring)
    return result[0]

f = open('hi.txt','r')
byte64Im = f.read()
print(analyze_user(byte64Im,byte64Im))