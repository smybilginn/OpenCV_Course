import cv2
import time

#video ismi
video_name = "MOT17-04-DPM.mp4"

#video içe aktarma capture-cap-
cap = cv2.VideoCapture(video_name)  
"""
cv2.VideoCapture() — OpenCV’de bir video kaynağını açmak için kullanılan bir sınıftır (class).

Bu kaynak:

- Bir video dosyası (.mp4, .avi, .mov vb.) olabilir.

- Bir kamera (bilgisayarın kamerası veya USB kamera) olabilir.

- Yani bu fonksiyon, OpenCV’ye şunu söyler:

“Ben bir video kaynağından görüntü almak istiyorum.”
"""
print("Genişlik:",cap.get((3)))
print("Yükselik:",cap.get((4)))
"""
cap.get(propId) → Kamera veya video kaynağından bir özelliğin değerini alır.

propId → Hangi özelliği istediğini belirten bir numara (ID).

3-Görüntü genişliği (piksel cinsinden)
4-Görüntü yüksekliği (piksel cinsinden)

"""

if cap.isOpened() == False:
    print("Hata")

# Sonsuz döngü: video bitene kadar her kareyi oku
while True:
    ret, frame = cap.read()
    # ret -> True (başarılı okuma) veya False (video bitti ya da hata)
    # frame -> okunan kare (görüntü verisi)
    
    if ret == True:
        time.sleep(0.01) #bunu kullanmazsak video çok hızlı akar
    
        cv2.imshow("video",frame)
        
    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

cap.release() #stop capture. Döngü bitince video kaynağını serbest bırak
cv2.destroyAllWindows() #tüm açık pencereleri kapatır
    
    