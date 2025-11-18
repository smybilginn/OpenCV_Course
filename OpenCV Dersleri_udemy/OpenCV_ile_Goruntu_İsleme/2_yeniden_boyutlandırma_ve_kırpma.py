import cv2

img = cv2.imread("lenna.png")

print("resim boyutu:",img.shape)
cv2.imshow("original",img)

#resized
imgResized = cv2.resize(img,(800,800))
print("Resized img shape", imgResized.shape)
cv2.imshow("img resized",imgResized)

#crop
imgCropped = img[:200,:300] #x ekseninden 200, y ekseninden 300
cv2.imshow("img cropped", imgCropped)


if img is None:
    print("Resim bulunamadı, dosya yolunu kontrol et!")
else:
    print("Resim Boyutu:", img.shape)
    cv2.imshow("orijinal", img)
    cv2.waitKey(0)              # Kullanıcı bir tuşa basana kadar bekler
    cv2.destroyAllWindows()     # Pencereleri kapatır
