import segno

qrcode = segno.make_qr("siema to ja https://github.com/juliazwierko")
# цвет - #2980B9, граница - 4, масштабирование - в 5 раз
qrcode.save("bluhhh_qr.png", dark="#2980B9", border=4, scale=5)



#Кодирование email
segno.helpers.make_email(to, cc=None, bcc=None, subject=None, body=None)
 
# Параметры:
# to -  кому письмо
# cc -  список получателей копии письма
# bcc -  список получателей слепой копии письма
# subject -  тема письма
# body -  текст письма



#Кодирование геокоординат
segno.helpers.make_geo(lat, lng)
 
# Параметры:
# lat -  широта
# lng -  долгота



#Кодирование настроек wifi
segno.helpers.make_wifi(ssid, password=None, security=None, hidden=False)
 
# Параметры:
# ssid -  SSID сети
# password -  пароль
# security -  тип аутентификации ("WEP" или "WPA").
# hidden -  является ли сеть скрытой



#Кодирование email:
from segno import helpers
qrcode = helpers.make_email("tom@gmail.com", cc=None, bcc=None, subject="Тема письма", body="Содержимое письма")
qrcode.save("email_qr.png", scale=5)
#Кодировнаие настроек wifi
from segno import helpers
qrcode = helpers.make_wifi(ssid="MyWifi", password="1234567890", security="WPA")
qrcode.save("wifi-access.png", scale=10)
