"""
Görselin nasıl okunacağı,
Nasıl görüntüleneceği,
Nasıl kaydedileceğini içerir
"""
import cv2

#ice aktarma
img = cv2.imread("messi.jpg",0) #0 resmi gray scale ile import eder

#gorsellestirme
cv2.imshow("ilk Resim",img)


k= cv2.waitKey(0) &0xFF
if k ==27: # ESC tuşu
    cv2.destroyAllWindows()
elif k == ord("s"): # "s" tuşuna basılırsa kaydet
    cv2.imwrite("messi_gray.png", img)