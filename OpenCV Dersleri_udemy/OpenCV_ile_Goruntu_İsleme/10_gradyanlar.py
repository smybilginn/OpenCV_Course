"""
Görüntü gradyanı, görüntüdeki yoğunluk (piksel değerleri)) veya renkteki yönlü bir değişikliktir.

Kenar algılamda kullanılır.
"""
# -------------------------------------------------------------
# TÜREV (DERIVATIVE) GÖRÜNTÜDE NE İŞE YARAR? - AÇIKLAMA
# -------------------------------------------------------------
# Türev matematikte "değişimin ölçüsü"dür.
# Görüntülerde türev almak, bir piksel ile yanındaki piksel arasındaki 
# parlaklık farkını ölçmek anlamına gelir.
#
# Eğer iki piksel arasında büyük fark varsa (örneğin koyudan birden beyaza geçiş),
# bu bir KENAR demektir. Türev bu keskin değişimleri yakalar.
#
# NEDEN TÜREV ALIYORUZ?
# ---------------------
# Çünkü görüntüdeki kenarları, sınırları ve ani parlaklık değişimlerini tespit etmenin
# en iyi yolu türev almaktır. Kenarlar, görüntüde bilgi taşıyan yerlerdir.
#
# Türev alınmazsa:
# - Kenarlar görünmez
# - Nesneler ayrıştırılamaz
# - Segmentasyon yapılamaz
# - Sobel, Laplacian, Canny gibi algoritmalar çalışmaz
#
# X ve Y YÖNÜNDE TÜREV
# ---------------------
# dx = 1, dy = 0 --> X yönünde türev (dikey kenarları bulur)
# dx = 0, dy = 1 --> Y yönünde türev (yatay kenarları bulur)
#
# SOBEL OPERATÖRÜ
# ---------------------
# Sobel filtresi aslında bir türev filtresidir:
# - Sobel X --> X yönünde parlaklık değişimi
# - Sobel Y --> Y yönünde parlaklık değişimi
#
# LAPACIAN
# ---------------------
# Laplacian ikinci türev alır (hem X hem Y yönünde).
# Kenarları daha güçlü ve her yönde yakalar.
#
# NEDEN CV_16S KULLANIYORUZ?
# ---------------------
# Türev negatif değer üretebilir.
# Örn: 20 - 150 = -130
# uint8 formatı negatif değer tutamaz! (0 ile 255 arası)
# Bu yüzden CV_16S veya CV_64F gibi signed (işaretli) formatlar kullanılır.
#
# ÖZET:
# ---------------------
# Türev = görüntüdeki değişimin miktarı
# Büyük türev = kenar
# Kenar bulma / nesne tespiti / segmentasyon için türev almak şarttır.
# -------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("sudoku.jpg",0)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("Orijinal Img")

# X Gradyanları bulma
#Aşağıdaki kod, Sobel X gradyanı (yatay kenar bilgisi) çıkarma işlemini yapıyor.
#Sobel filtresi, görüntü üzerindeki gradyanı, yani parlaklık değişimlerini (kenarları) bulmak için kullanılır.
"""Bu filtre:

dx = 1, dy = 0 → X yönünde kenar bulma (yatay kenarların dikliği)

dx = 0, dy = 1 → Y yönünde kenar bulma (düşey kenarların dikliği)

Bu kodda x yönündeki gradyan hesaplanıyor.

ksize = 5

Kullanılan Sobel kernelinin boyutu.

ksize=1 → basit türev

ksize=3 → daha yumuşak

ksize=5 → daha güçlü, daha net kenarlar

#Kernel = görüntünün üzerinde gezdirilen küçük bir matristir.
#Bu matris, bir pikselin yeni değerinin nasıl hesaplanacağını belirler.

Üretilen sonuç pikselin sağındaki ve solundaki parlaklık farkını bulur.

Büyük pozitif değer → sağ taraf daha parlak

Büyük negatif değer → sol taraf daha parlak

Sıfıra yakın → kenar yok
"""
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy =0, ksize = 5 )
plt.figure()
plt.imshow(sobelx, cmap = "gray")
plt.axis("off")
plt.title("Sobelx Img")

#y gradyan
sobely = cv2.Sobel(img,ddepth = cv2.CV_16S,dx = 0,dy = 1,ksize = 5)
plt.figure()
plt.imshow(sobely, cmap = "gray")
plt.axis("off")
plt.title("Sobely Img")


# x ve y birlikte görmek için Laplacian gradyan kullanılır
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap ="gray")
plt.axis("off")
plt.title("Laplacian")

"""Laplacian ne yapıyor?

Sobel’den farklı olarak hem X hem Y yönünde ikinci türev alır.

Tüm kenarları aynı anda ortaya çıkarır.

Daha hassas ve güçlü bir kenar bulucudur."""





