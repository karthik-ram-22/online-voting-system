from base64 import encode
from email.mime import base
import cv2
import face_recognition
import sys
import base64
from PIL import Image
import io
import numpy as np

def take_picture(name):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(f'Picture{name}.jpg', frame)
    cv2.destroyAllWindows()
    cap.release()

def analyze_user(base64_string):
    # baseimg = face_recognition.load_image_file(f'Picture{name}.jpg')
    # baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    baseimg = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)


    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)

    cv2.imshow("Test", baseimg)
    cv2.waitKey(0)

    sampleimg = face_recognition.load_image_file("Pictureagain.jpg")
    sampleimg = cv2.cvtColor(sampleimg, cv2.COLOR_BGR2RGB)

    try:
        samplefacetest = face_recognition.face_locations(sampleimg)[0]
        encodesamplefacetest = face_recognition.face_encodings(sampleimg)[0]
    except IndexError as e:
        print(e)
        sys.exit()

    result = face_recognition.compare_faces([encodemyface], encodesamplefacetest)
    resultstring = str(result)
    print(resultstring)




# take_picture("subject2")
f = open('hi.txt','r')
byte64Im = f.read()

analyze_user(byte64Im)
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    img = Image.open(io.BytesIO(imgdata))
    opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    return opencv_img 

# stringToRGB(byte64Img)
# imgdata = base64.b64decode(byte64Img)
# print(imgdata)