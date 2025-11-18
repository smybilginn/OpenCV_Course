import cv2

cap = cv2.VideoCapture(0)
"""cv2.VideoCapture ile bir video kaynağı açar.

0 → bilgisayardaki varsayılan kamerayı (webcam) ifade eder.

Eğer 1, 2 gibi bir sayı yazarsan, başka kameraları kullanırsın.

Eğer "video.mp4" yazarsan, bir video dosyasını açar.

Bu satırdan sonra cap adında bir VideoCapture nesnesi oluşur.
Bu nesne üzerinden kameradan görüntü alınabilir."""

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
"""Kameradan gelen görüntünün genişlik ve yüksekliğini (çözünürlüğünü) alır.

cv2.CAP_PROP_FRAME_WIDTH → kare genişliği (örnek: 640)

cv2.CAP_PROP_FRAME_HEIGHT → kare yüksekliği (örnek: 480)

int() → bu değerleri tamsayıya çevirir çünkü cap.get() float döndürür."""

print(width,height)

#video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width,height))

while True:
    ret, frame = cap.read()
    cv2.imshow("video",frame)
    
    #☻save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()