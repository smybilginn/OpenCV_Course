"""
Erozyon:
    - Erozyonun temel fikri sadece toprak erezyonu gibidir, ön plandaki nesnenin sınırlarını aşındırır.
Genişleme:
    - Erozyonun tam tersidir.
    -Görüntüdeki beyaz bölgeyi artırır.
Açma:
    - Açılma, erozyon + genişlemedir.
    - Gürültünün giderilmesi için faydalıdır.

Kapatma:
    -Kapanış, açmanın tersidir.
    -Genişleme + erozyon
    - Ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.

Morfolojik Gradyan:
    -Bir görüntünün genişlemesi ve erozyonu arasındaki farktır.
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("datai_team.jpg",0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("Orijinal img")

#Erozyon - sınırlar küçültülür
kernel = np.ones((5,5), dtype=np.uint8 )
result = cv2.erode(img, kernel,iterations=1)
"""5×5 boyutunda bir kernel (yapı elemanı) oluşturulur.

Erozyon uygulanır → küçük beyaz noktalar kaybolur."""
plt.figure()
plt.imshow(result, cmap = "gray")
plt.axis("off")
plt.title("Erozyon")


#genişleme (dilation)
result2 = cv2.dilate(img, kernel, iterations = 1) #Erozyonun tam tersi işlem.
plt.figure()
plt.imshow(result2, cmap = "gray")
plt.axis("off")
plt.title("Genisleme")


 #Açılma için White Noise
whiteNoise = np.random.randint(low = 0, high = 2, size = img.shape[:2])
whiteNoise = whiteNoise*255
"""0 ve 1'lerden oluşan rastgele matris → beyaz noktalar

255 ile çarpılarak tam beyaz piksele dönüştürülür."""
plt.figure()
plt.imshow(whiteNoise, cmap = "gray")
plt.axis("off")
plt.title("White Noise")

noise_img = whiteNoise + img #Görüntü üzerine beyaz noktalar eklenir
plt.figure()
plt.imshow(noise_img, cmap = "gray")
plt.axis("off")
plt.title("img with White Noise")


#Açılma Yöntemi (erozyon + genişleme)
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening,cmap = "gray")
plt.axis("off")
plt.title("Acilma")

#Kapatma için black noise
blackNoise = np.random.randint(low = 0, high = 2, size = img.shape[:2])
blackNoise = blackNoise*-255
black_noise_img = blackNoise + img
"""0 veya –255 değerleri üretir → siyah noktalar.

Görüntüye siyah gürültü eklenir."""
plt.figure()
plt.imshow(black_noise_img, cmap = "gray")
plt.axis("off")

black_noise_img[black_noise_img <= -245] = 0 #Aşırı siyah piksel değerlerini sıfırlanıyor
plt.figure()
plt.imshow(black_noise_img, cmap = "gray")

#Kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing,cmap = "gray")
plt.axis("off")

plt.title("Kapatma")

# Morphological Gradient it is edge detection
# It is the difference between dilation and erosion of an image.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
"""Bu işlem:
 Kenarları çıkarır
 Kenar tespiti için morfolojik yöntemdir

Sonuç: Siyah–beyaz hatlar şeklinde kenarlar görünür."""
plt.figure()
plt.imshow(gradient,cmap = "gray")
plt.axis("off")
plt.title("Morfolojik  Gradyan")




































