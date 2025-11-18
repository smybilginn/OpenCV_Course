"""
Bu kütüphane matrisler için hesaplama kolaylığı sağlar 

"""

import numpy as np

#1*15 boyutunda bir array 
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) # arrayin boyutu

dizi2 = dizi.reshape(3,5) #Bu satır diziyi yeniden şekillendirir (reshape):

print("Şekil: ", dizi2.shape) #shape, dizinin şeklini (satır, sütun sayısını) verir.
print("Boyut: ", dizi2.ndim) #dizinin boyut sayısı
print("Veri Tipi: ", dizi2.dtype.name) #dizideki veri tipi (data type)
print("Boy: ", dizi2.size) #dizideki toplam eleman sayısı

#array type
print("Type: ",type(dizi2))

#2 boyutlu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])
print(dizi2D)

#sıfırlardan oluşan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

#birlerden oluşan bir array
bir_dizi = np.ones((3,4))
print(bir_dizi)

#bos array
bos_array = np.empty((3,4))
print(bos_array)

#arrange(x,y,basamak)
dizi_aralik = np.arange(10,50,5) #10'dan başla 50'ye kadar git her seferinde 5 artır.
print(dizi_aralik)

#linspace(x,y,basamak)
dizi_boslık = np.linspace(10,20,5) #10'dan başla 50'ye kadar git toplamda 5 sayı olsun
print(dizi_boslık)

#float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

#matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

#dizi elemanı toplama
print(np.sum(a))

#max değer
print(np.max(a))

#min değer
print(np.min(a))

#ortalama
print(np.mean(a))

#medyan
print(np.median(a))

#rastgele sayı üretme (0,1)
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

#index
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk dört elemanı
print(dizi[:4])

#dizinin terisni alma
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1. satır ve 1. sütununda bulunan ekemanı çağırma
print(dizi2D[1,1])

#dizinin 1. sütununun tüm satırlar
print(dizi2D[:,1])

#satır 1, sütun 1,2,3
print(dizi2D[1,1:4])

#dizinin son satır tüm sütunları
print(dizi2D[-1:])

#
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

#vektör haline getirme
vektor = dizi2D.ravel()
print(vektor)

#max sayının indeksi
max_sayinin_indeksi = vektor.argmax()
print(max_sayinin_indeksi)





















