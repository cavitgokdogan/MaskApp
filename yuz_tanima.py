""" kameraya gösterilen yüzleri, veri setimizdeki yüzlerle karşılaştırarak tanıyacak olan modül"""

import cv2      #opencv kütüphanesi eklendi
import numpy as np
import requests
import pymongo
from Mail import sendMail

"""
myDatabase = pymongo.MongoClient("connection_url") #maskapp adlı veritabanımıza bağlandık
users = myDatabase.test.users # maskapp adlı veritabanımızın users adlı collection'ınını users adlı bir değişkene atadık.
url = "url..."
headers={
    "content-type": "application/json"
}

def dataBaseAdd(number):
    user = users.find_one({"number":number})
    if(user):
        requests.put(f"{url}/{str(user['_id'])}",headers=headers)
"""
  
taniyici = cv2.face.LBPHFaceRecognizer_create()     #yüz tanıyıcı olusturuldu
taniyici.read("deneme/deneme.yml")                  #tanıyıcı deneme.yml dosyasını okuyacak

yolsiniflandirici = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

yuzsiniflandirici = cv2.CascadeClassifier(yolsiniflandirici)    #kullanılacak yol atandı
#font = cv2.FONT_HERSHEY_SIMPLEX #yazi tipi belirlendi
vid_cam = cv2.VideoCapture(0)   # Bilgisayara bağlı kameradan alınan görüntü vid_cam değişkenine atandı.

#Kişilere aynı derste 1 kez ceza yazılması için flag yapısı kullanıldı.
calistiC = True
calistiS = True
calistiA = True
calistiM = True
calistiAG = True

while(True):
    ret, kamera = vid_cam.read()    #vid_cam den okunan image kameraya atandı
    gri = cv2.cvtColor(kamera, cv2.COLOR_BGR2GRAY)  #Kameradan alınan görüntü daha iyi bir tespit için BGR den gri ye çevirildi.
    yuzler = yuzsiniflandirici.detectMultiScale(gri, 1.2, 5)    #gri tonlamanın alt üst(koyuluk) sınırları belirlendi

    for(x, y, w, h) in yuzler:
        cv2.rectangle(kamera, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)   #Yüzün çevresini çevreleyen dikdörtgen.
        #Id ve conf degerini dondurur
        Id, conf = taniyici.predict(gri[y: y+h, x: x+w])    #?????

        print(Id)
        print(100 - conf) #Doğruluk oranı
        print("\n")

        #Id leri tanıtılan kişilerin tanındıktan sonra ceza eklendiği kısım.
        
        if(Id == 1):
            name = "Cavit"
            number = "032090079"
            email = "032090079@ogr.uludag.edu.tr"
            if calistiC:
                #sendMail(email)
                #dataBaseAdd(number)
                calistiC = False
        """
        elif(Id == 2):
            name = "Semih"
            number="032090010"
            email = "032090010@ogr.uludag.edu.tr"
            if calistiS:
                calistiS = False
                sendMail(email)
                dataBaseAdd(number)
        elif(Id == 3):
            name = "Merve"
            number = "032090007"
            email = "032090007@ogr.uludag.edu.tr"
            if calistiM:
                calistiM = False
                sendMail(email)
                dataBaseAdd(number)
        elif(Id == 4):
            name = "AlperenM"
            number = "032090020"
            email = "032090020@ogr.uludag.edu.tr"
            if calistiA:
                calistiA = False
                sendMail(email)
                dataBaseAdd(number)
        elif(Id == 5):
            name = "AlperenG"
            number = "032090078"
            email = "032090078@ogr.uludag.edu.tr"
            if calistiAG:
                calistiAG = False
                sendMail(email)
                dataBaseAdd(number)
        """
        #yuz tanıma için cerceve ebatları belirlendi
        cv2.rectangle(kamera, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
        
        #yazılacak ismin boyutları,rengi ve kalınlığı belirlendi
        cv2.putText(kamera, str(name), (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

    cv2.imshow("Goruntu", kamera)    #Kameradan alınan görüntü ekranda gösterilir.
    #Yuz tanıma programının sonlandırılması.
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vid_cam.release()
cv2.destroyAllWindows()