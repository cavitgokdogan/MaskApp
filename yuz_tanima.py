""" kameraya gösterilen yüzleri, veri setimizdeki yüzlerle karşılaştırarak tanıyacak olan modül"""

import cv2      #opencv kütüphanesi eklendi
import numpy as np
import requests
import pymongo
import json
import matplotlib.pyplot as plt
from Mail import sendMail


stream_url = f"rtsp://SimaProject:Yumurta1@192.168.1.184:554/stream1"
"""
myDatabase = pymongo.MongoClient("mongodb+srv://semih:semih123@cluster0.ceuft.mongodb.net/test?retryWrites=true&w=majority") #maskapp adlı veritabanımıza bağlandık
users = myDatabase.test.users # maskapp adlı veritabanımızın users adlı collection'ınını users adlı bir değişkene atadık.
url = "https://maskapp-backend.onrender.com/users"
headers={
    "content-type": "application/json"
}
"""
"""
def dataBaseAdd(number):
    user = users.find_one({"number":number})
    if(user):
        requests.put(f"{url}/{str(user['_id'])}",{"cezapuani" : user["cezapuani"] + 10},headers=headers)
        print(f"{url}/{str(user['_id'])}")
"""
"""
def dataBaseAdd(number):
    user = users.find_one({"number": number})
    if user:
        updated_data = {"cezapuani" : user["cezapuani"] + 10}
        requests.put(f"{url}/{str(user['_id'])}", data=json.dumps(updated_data), headers=headers)
        print(f"{url}/{str(user['_id'])}")
"""

  
recognizer = cv2.face.LBPHFaceRecognizer_create()     #yüz tanıyıcı olusturuldu
recognizer.read("face_yml/deneme.yml")                  #tanıyıcı deneme.yml dosyasını okuyacak

yolsiniflandirici = "haarcascade_frontalface_default.xml"
accuracy_rates = []

yuzsiniflandirici = cv2.CascadeClassifier(yolsiniflandirici)    #kullanılacak yol atandı
#font = cv2.FONT_HERSHEY_SIMPLEX #yazi tipi belirlendi
vid_cam = cv2.VideoCapture(stream_url)   #(stream_url) Bilgisayara bağlı kameradan alınan görüntü vid_cam değişkenine atandı.

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
        Id, conf = recognizer.predict(gri[y: y+h, x: x+w])    #?????

        print(Id)
        accuracy_rate = 100 - conf
        print(f"{accuracy_rate: .2f}") #Doğruluk oranı
        accuracy_rates.append(accuracy_rate)
        print("\n")

        #Id leri tanıtılan kişilerin tanındıktan sonra ceza eklendiği kısım.
        
        if(Id == 1):
            name = "Cavit"
            number = "032090079"
            email = "032090079@ogr.uludag.edu.tr"
            """
            if calistiC:
                #sendMail(email)
                dataBaseAdd(number)
                calistiC = False
            """
        
        elif(Id == 2):
            name = "Seher"
            number="032090010"
            email = "032090010@ogr.uludag.edu.tr"
            """
            if calistiS:
                calistiS = False
                sendMail(email)
                dataBaseAdd(number)
            """
        
        elif(Id == 3):
            name = "Badeser"
            number = "032090007"
            email = "032090007@ogr.uludag.edu.tr"
            """
            if calistiM:
                calistiM = False
                sendMail(email)
                dataBaseAdd(number)
            """
        elif(Id == 4):
            name = "Sevval"
            number = "032090020"
            email = "032090020@ogr.uludag.edu.tr"
            """
            if calistiA:
                calistiA = False
                sendMail(email)
                dataBaseAdd(number)
            """
        elif(Id == 5):
            name = "Ahmet"
            number = "032090078"
            email = "032090078@ogr.uludag.edu.tr"
            """
            if calistiAG:
                calistiAG = False
                sendMail(email)
                dataBaseAdd(number)
            """
        
        #yuz tanıma için cerceve ebatları belirlendi
        cv2.rectangle(kamera, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
        
        #yazılacak ismin boyutları,rengi ve kalınlığı belirlendi
        cv2.putText(kamera, str(name), (x - 30, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

    
    win_name = "goruntu"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win_name, 800, 600)


    cv2.imshow(win_name, kamera)    #Kameradan alınan görüntü ekranda gösterilir.
    #Yuz tanıma programının sonlandırılması.
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vid_cam.release()
cv2.destroyAllWindows()

plt.plot(accuracy_rates)
plt.title('Accuracy Rate Over Time')
plt.xlabel('Time')
plt.ylim(30, 100)
plt.ylabel('Accuracy Rate')
plt.show()
