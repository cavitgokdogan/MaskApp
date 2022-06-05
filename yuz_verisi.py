"""veri setimizi, veri klasörü içine olusturduğumuz modül"""

import cv2      #opencv kütüphanesi eklendi

vid_cam = cv2.VideoCapture(0)   #video kamera tanımlandı

yuz_dedektor = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

yuz_ismi = 1    #her farklı yüz için farklı numara tanımlanacak
sayi = 1        #çekilecek fotoğraf sayısı

while(True):
    _, resim_cerceve = vid_cam.read()   #kamera okutuldu

    gri = cv2.cvtColor(resim_cerceve, cv2.COLOR_BGR2GRAY) #gri tonlama eklendi
    
    #Eger yuze benzeyen ufak bolgeler karistiriliyorsa minSize = () eklenebilir. Default 130,130
    yuzler = yuz_dedektor.detectMultiScale(gri, 1.3, 5)#Resimdeki yüzlerin yerleri tespit edildi. Gri tonlamanın alt üst(koyuluk) sınırları belirlendi

    for(x, y, w, h) in yuzler: #yuzu algılayacak çerçeve ebatları 

        #cerceve kalınlıgı ve rengı
        cv2.rectangle(resim_cerceve, (x + 5, y + 10), (x + w, y + h), (0, 0, 255), 2)
        sayi += 1

        #resimler veri klasörüne aşağıdaki şekilde yazdırılır
        cv2.imwrite("veri/User." + str(yuz_ismi) + '.' + str(sayi) + ".jpg", gri[y: y+h, x: x+w])
       
        #kameraya göster komutu atandı
        cv2.imshow('cerceve' , resim_cerceve)   #ARASTIR

        #kameradan çıkış tuşu ve gecikme süresi belirlendi
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    elif sayi > 100: #çekilecek fotoğraf sayısı için üst sınır belirlendi
        break

vid_cam.release()   #kamera durduruldu
cv2.destroyAllWindows() #tum pencereler kapatıldı