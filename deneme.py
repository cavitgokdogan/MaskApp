from email.mime import image
import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create() 

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    yuzornekleri = []   
    isimler = []        

    for imagePaths in imagePaths:
        #P[3] & L[1]
        PIL_img = Image.open(imagePaths).convert('L')

        #Görüntüleri 8 bitlik numpy dizisi halıne dönüştürdük
        img_numpy = np.array(PIL_img, 'uint8')

        #dosya adından kişi numarasını ayırdık,id  değişkenine atadık
        id = int(os.path.split(imagePaths)[-1].split(".")[1])
        print(id)

        #img_numpy görüntü numpy dizisinde bulunan yüz alanlarını bulup yuzler listesine attık
        yuzler = detector.detectMultiScale(img_numpy)

        for(x, y, w, h) in yuzler:
            yuzornekleri.append(img_numpy[y:y + h, x: x + w])
            isimler.append(id)

    return yuzornekleri, isimler

yuzler, isimler = getImagesAndLabels("veri")
recognizer.train(yuzler, np.array(isimler))

recognizer.save("face_yml/deneme.yml") 