# -------------------------------------------------------------
# GÖRÜNTÜ İŞLEMEDE HISTOGRAM NEDİR? - AÇIKLAMA
# -------------------------------------------------------------
# Histogram, bir görüntüdeki piksel parlaklık değerlerinin dağılımını gösteren
# bir grafiktir. Her parlaklık seviyesinin (0-255) kaç tane pikselde bulunduğunu
# gösterir.
#
# x ekseni  : parlaklık değerleri (0 = siyah, 255 = beyaz)
# y ekseni  : o parlaklıktaki piksel sayısı
#
# Histogram, görüntünün:
# - karanlık mı
# - aydınlık mı
# - düşük kontrastlı mı
# - yüksek kontrastlı mı
# olduğunu anlamamızı sağlar.
#
# ÖRNEK YORUMLAR:
# ---------------
# 1) Histogram solda yoğun ise --> görüntü karanlık (düşük parlaklık)
# 2) Histogram sağda yoğun ise --> görüntü aydınlık (yüksek parlaklık)
# 3) Histogram ortada yoğun ise --> görüntü dengeli
# 4) Histogram dar ve sıkışık ise --> düşük kontrast (soluk/flat görüntü)
# 5) Histogram geniş yayılmış ise --> yüksek kontrast (keskin görüntü)
#
# NEDEN ÖNEMLİ?
# -------------
# Çünkü histogram bir görüntünün kalite bilgisini verir.
# Histogram sayesinde:
# - Parlaklık ayarlama
# - Kontrast iyileştirme (Histogram Equalization)
# - Threshold belirleme
# - Gürültü analizi
# - Görüntü kalibrasyonu
# gibi işlemler yapılabilir.
#
# HISTOGRAM EŞİTLEME (Equalization) NEDİR?
# ----------------------------------------
# Histogramın daha geniş yayılması için yapılan işlemdir.
# Sonuç: daha yüksek kontrastlı görüntü.
#
# cv2.equalizeHist() ile yapılır.
#
# ÖZET:
# -----
# Histogram = piksel dağılımı grafiği.
# Görüntünün parlaklık ve kontrast yapısını anlamak için kullanılır.
# Görüntü iyileştirme işlemlerinin temelidir.
# -------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img  = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #cv2 den default gelen BGR değerlerini RGB formatına dönüştürdük
plt.figure()
plt.imshow(img_vis)

#kac piksel var
print(img.shape)

#histogram cizdirme
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure()
plt.plot(img_hist)
"""
channels=[0] → Blue kanalı

histSize=[256] → 0–255 arası parlaklık değerleri

Histogram görüntünün mavi kanal piksel dağılımını gösterir."""


color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256])
    plt.plot(hist, color = c)
"""Döngü görüntünün tüm kanalları için histogram çıkarır.

i=0 → Blue

i=1 → Green

i=2 → Red

Matplotlib çizgi rengini kanal rengi ile eşleştirir.

Bu grafik görüntünün renk dağılımını çok güzel gösterir."""

#maskeleme
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate_vis)

print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure()
plt.imshow(mask, cmap = "gray")
"""
Tamamen siyah (0) bir maske oluşturuyor.

Maske görüntünün yükseklik × genişliği kadar, tek kanallı."""


mask[1500:2000, 1000:2000] = 255
plt.figure()
plt.imshow(mask, cmap = "gray")
"""
Bu işlem maskenin belirli bir bölgesini beyaz (255) yapar.

Beyaz → gösterilecek alan

Siyah → gizlenecek alan

Maske artık “burayı göster” demiş oluyor."""

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis,mask=mask)
plt.figure()
plt.imshow(masked_img_vis, cmap = "gray")
"""
Sadece maskenin beyaz olduğu kısmı görünür.

Siyah olan yerler sıfırlanır (0 = siyah olur)
"""

masked_img = cv2.bitwise_and(golden_gate, golden_gate,mask=mask)
masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask =None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(masked_img_hist)


# histogram equalization :
# We will learn the concepts of histogram equalization and use it to improve the contrast of our images.
img = cv2.imread("hist_equ.jpg",0)
plt.figure()
plt.imshow(img, cmap = "gray")

img_hist = cv2.calcHist([img], channels=[0], mask =None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist, cmap = "gray")
"""
Histogramı genişletir

Kontrastı artırır

Karanlık bölgeleri aydınlatır
"""

eq_img_hist = cv2.calcHist([eq_hist], channels=[0], mask =None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(eq_img_hist)
"""
Histogram eşitlemeden sonra histogram daha geniş yayılır.
Kontrast artar, görüntü daha net hale gelir.
"""






