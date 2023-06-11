"""veri setimizi eğittiğimiz modül"""

from email.mime import image
import imp
import cv2
import os
import numpy as np
from PIL import Image

#verisetimizin eğitimini aşağıdaki komutla tanıyıcı üzerinden yapacağız
tanıyıcı = cv2.face.LBPHFaceRecognizer_create() 

#görüntülerdeki yuz alanlarını ayırmak için aşağıdaki xml filtresini kullanacağız
dedektor = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#görüntü etiketlerimizi almak için kullanacağımız fonksiyon
def getImagesAndLabels(path):
    
    #imagePaths listesi, path klasörü içinde yer alan dosyaların listesidir
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    yuzornekleri = []   #yuz görüntülerini tutacak liste
    isimler = []        #her bir görüntünün etiketini tutacak liste

    #imagePaths listesinin her bir elemanını kullanarak ilgili resmi okuyup
    #griye dönüştürdük
    for imagePaths in imagePaths:
        #P[3] & L[1]
        PIL_img = Image.open(imagePaths).convert('L')

        #Görüntüleri 8 bitlik numpy dizisi halıne dönüştürdük
        img_numpy = np.array(PIL_img, 'uint8')

        #dosya adından kişi numarasını ayırdık,id  değişkenine atadık
        id = int(os.path.split(imagePaths)[-1].split(".")[1])
        print(id)

        #img_numpy görüntü numpy dizisinde bulunan yüz alanlarını bulup yuzler listesine attık
        yuzler = dedektor.detectMultiScale(img_numpy)

        #yuzler listesini döngüye sokup her bir görüntüyü yuzornekleri,
        #  ona karşılık gelen etiketi ise isimler listesine ekliyoruz.
        for(x, y, w, h) in yuzler:
            yuzornekleri.append(img_numpy[y:y + h, x: x + w])
            isimler.append(id)

    return yuzornekleri, isimler

yuzler, isimler = getImagesAndLabels("veri")    #listelerimiz olustu
tanıyıcı.train(yuzler, np.array(isimler))   #veri setimizi eğitiyoruz

#eğitilmiş veriseti bilgilerimizi; deneme klasörü içindeki deneme.yml dosyamıza kaydettik
tanıyıcı.save("deneme/deneme.yml") 