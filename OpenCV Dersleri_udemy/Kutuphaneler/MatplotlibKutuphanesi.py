"""
Matplotlib, Python’daki en güçlü görselleştirme (plotlama) kütüphanelerinden biridir.

Temel görevi:

Verileri, grafikleri ve görüntüleri görsel olarak göstermek.

Yani, NumPy sayılarla çalışır,
Pandas verileri düzenler,
Matplotlib bunları görselleştirir.

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure() #figürü açma
plt.plot(x, y, color = "red", alpha = 0.7, label = "line")
"""
plot() → çizgi grafiği çizer.

x ve y: grafikteki noktaların koordinatları

color="red" → çizginin rengi

alpha=0.7 → saydamlık (1 = opak, 0 = tamamen şeffaf)

"""
plt.scatter(x, y, alpha=0.4, label= "scatter")
"""
scatter() → nokta (dağılım) grafiği çizer.

Aynı x ve y değerlerini nokta nokta gösterir.

alpha=0.4 → biraz saydam yapar.

label="scatter" → legend’de “scatter” olarak gözükür.
"""
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True) #Grafiğe ızgara çizgileri ekler.
plt.xticks([0,1,2,3,4,5]) #X ekseninde hangi değerlerin etiketleneceğini belirtir.
plt.legend() #Grafikte “line” ve “scatter” yazılı bir kutucuk çıkar.
plt.show() #figürü kapatma


#birden fazla plotu tek figür içerisine çizdirme
fig, axes = plt.subplots(2,1, figsize=(9,7))
"""9x7 boyutlarında bir figür (ana grafik penceresi) oluştur
ve içinde 2 satır, 1 sütun olacak şekilde 2 alt grafik (subplot) oluştur."""
fig.subplots_adjust(hspace = 0.5)
"""Bu satır alt grafikler arasındaki dikey boşluğu (height space) ayarlıyor.
🔹 Küçük hspace → grafikler birbirine yakın
🔹 Büyük hspace → grafikler arası mesafe artar

Örneğin:
"""

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(x,y)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")

#random resim
plt.figure()
img = np.random.random((50,50))
plt.imshow(img,cmap = "gray")
plt.axis("off")
plt.show()






















