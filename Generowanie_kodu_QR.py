import segno
 
qrcode = segno.make_qr("siema to ja https://github.com/juliazwierko")
# цвет - #2980B9, граница - 4, масштабирование - в 5 раз
qrcode.save("metanit_qr.png", dark="#2980B9", border=4, scale=5)
