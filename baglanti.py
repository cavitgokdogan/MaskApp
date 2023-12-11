import cv2

# Kamera adresini girin
camera_ip = "192.168.1.157"  # Kameranın IP adresini buraya girin

# Kamera akışı için bağlantı URL'sini oluşturun
stream_url = f"rtsp://SimaProject:Yumurta1@192.168.1.117:554/stream1"  # Varsayılan kimlik bilgileriyle

# Video akışını başlatın
cap = cv2.VideoCapture(stream_url)

# Kamera bağlantısı başarılıysa devam edin
if cap.isOpened():
    while True:
        # Kameradan görüntüyü alın
        ret, frame = cap.read()

        if ret:
            # Görüntüyü işleyin (örneğin, burada kameradan alınan görüntüyü gösterebilirsiniz)
            cv2.imshow("Kamera Görüntüsü", frame)

        # Çıkış için "q" tuşuna basılmasını kontrol edin
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Temizlik yapın ve çıkın
cap.release()
cv2.destroyAllWindows()
