import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3),np.uint8) #3siyah bir resim
print(img.shape)

cv2.imshow("siyah",img)

#çizgi
#resim, başlangıç noktası,bitiş noktasi,renk,çizgi kalınlığı
cv2.line(img, (0,0), (512,512),(0,255,0),3)  #BGR-RGB 
cv2.imshow("cizgi",img)

#dikdortgen
#resim,başlangıç,bitiş,renk
cv2.rectangle(img, (0,0),(256,256), (255,0,0))
cv2.imshow("dikdortgen",img)

#cember
#♦resim,merkez,yaricap,renk,icinin doluluğu(her zaman gerekli değil)
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("circle",img)


#metin
#resim, başlangıç noktası, font, kalınlığı, renk
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Yazi", img)

if img is None:
    print(" Resim bulunamadı, dosya yolunu kontrol et!")
else:
    print("Resim Boyutu:", img.shape)
    cv2.waitKey(0)              # Kullanıcı bir tuşa basana kadar bekler
    cv2.destroyAllWindows()     # Pencereleri kapatır