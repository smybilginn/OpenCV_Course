# opencv kütüphanesini içe aktaralım
import cv2

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("odev1.jpg",0)

# resmi çizdirelim
cv2.imshow("odev-1",img)

# resmin boyutuna bakalım
print("Boyut:", img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
imgResized = cv2.resize(img,  (688, 454))
plt.figure()
plt.imshow(imgResized, cmap="gray")
plt.title("Img Resized")

# orjinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv2.putText(img, "Kopek",(350,350), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
cv2.imshow("Yazi", img)

#  orjinal resme 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim
_, thresh_img = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
cv2.imshow('Threshold', thresh_img)

# orjinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX =7)
cv2.imshow("Gaussian Blur", gb)

# orjinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)

# orhinal resmin histogramını çizdirelim
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img_hist)



