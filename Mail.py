import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(email):
        
    fromMail = "ornekmail@gmail.com"
    password = r'orneksifre'
    toMail = email

    msg = "Sevgili öğrencimiz lütfen bir sonraki dersinizde maskenizi takınız "

    mesaj = MIMEMultipart()
    mesaj["From"] = fromMail      # Gönderen kişi
    mesaj["To"] = toMail          # Alıcı
    mesaj["Subject"] = "Python Smtp ile Mail Gönderme" # Konu
    mesaj.attach(MIMEText(msg, 'plain'))

    sonMesaj = mesaj.as_string()

    eposta_sunucusu = smtplib.SMTP_SSL("smtp.gmail.com",465)
    eposta_sunucusu.login(fromMail,password)
    eposta_sunucusu.sendmail(fromMail,toMail,sonMesaj)
   
