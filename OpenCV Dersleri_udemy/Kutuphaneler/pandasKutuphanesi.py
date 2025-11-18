"""
- Pandas, temelde veri analizi ve veri yönetimi için geliştirilmiş bir kütüphanedir.
Yani görüntünün kendisini işlemekten çok, görüntülerle ilgili bilgileri (meta-verileri) düzenlemek için kullanılır

Pandas, bu görüntülere ait bilgileri tablo (DataFrame) şeklinde yönetmekte çok güçlüdür.

- hızlı, güçlü ve esnektir. 

"""

import pandas as pd

#dictionary oluştur
dictionary = {"isim" :["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  :[15,16,17,33,45,66],
              "maas"  :[100,150,240,350,110,220]}

veri = pd.DataFrame(dictionary)  #Veriyi DataFrame’e çevirmemizin temel nedeni, veriyi düzenli, erişilebilir ve analiz edilebilir bir tablo yapısına kavuşturmaktır.

print(veri)

#ilk 5 satır
print(veri.head())

#sütun
print(veri.columns)

#veri bilgisi
print(veri.info())

#verinin içerisinde bulunan istatistiksel bilgiler
print(veri.describe())

#yas sütununu tek görselleştirme
print(veri["yas"])

#sütun ekleme
veri["sehir"] = ["Ankara","İstanbul","Konya","İzmir","Bursa","Antalya"]
print(veri)

#sadece yas sütunun tüm verileri
print(veri.loc[:,"yas"])

#yas sütunun içerisindeki ilk üç satır
print(veri.loc[:2,"yas"])

#yas ve sehir sütunları arası 3 satır alma
print((veri.loc[:2,"yas":"sehir"]))

#isim VE yas ilk 3 sütun
print(veri.loc[:2,["yas","isim"]])

#satırları tersten yardırma
print(veri.loc[::-1,:])

#yas with iloc (index location)
print(veri.iloc[:,1]) #iloc — Pandas DataFrame’lerde satır ve sütunlara “indeks numaralarıyla” erişmek için kullanılır.

#ilk 3 satır ve yas ve isim
print(veri.iloc[:2,[0,1]])

#Filtreleme
dictionary = {"isim" :["ali","veli","kenan","murat","ayse","hilal"],
              "yas"  :[15,16,17,33,45,66],
              "sehir":["İzmir","Ankara","Konya","Ankara","Ankara","Antalya"]}

veri = pd.DataFrame(dictionary)
print(veri)

#yaşa göre bir filtre oluşturma yas>22
filtre1 = veri.yas > 22
filtrelenmis_veri = veri[filtre1]
print(filtrelenmis_veri)

#ortalama yas
ortalama_yas = veri.yas.mean()
print(ortalama_yas)

veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

#birlestirme
dic_1 = {"isim" : ["ali","veli","kenan"],
         "yas" : [15,16,17],
         "sehir": ["izmir","ankara","konya"]}

veri = pd.DataFrame(dic_1)

dic_2 = {"isim" : ["murat","ayse","hilal"],
         "yas" : [25,26,27],
         "sehir": ["antalya","ankara","konya"]}

veri2 = pd.DataFrame(dic_2)

#dikey birleştirme
veri_dikey = pd.concat([veri,veri2],axis =0)

#yatay birleştirme
veri_yatay = pd.concat([veri,veri2], axis = 1)


#axis = 0 dikey y ekseni
#axis = 1 yatay x ekseni