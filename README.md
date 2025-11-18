# OpenCV_Course
Udemy OpenCV course training codes

# 🚀 Python Görüntü/Video İşleme ve Veri Bilimi Temelleri

Bu depo, aldığım kurslar ve bireysel çalışmalar sonucunda Python'ın güçlü kütüphaneleri olan **OpenCV**, **NumPy**, **Pandas** ve **Matplotlib**'i kullanarak gerçekleştirdiğim temel alıştırmaları ve uygulamaları içermektedir.

Görüntü, video işleme ve veri manipülasyonu yeteneklerimi sergilemek amacıyla hazırlanmış, başlangıç seviyesindeki konuları kapsayan bir koleksiyondur.

---

## 📂 Proje İçeriği

Proje, üç ana başlık altında toplanmış temel Python kütüphane uygulamalarından oluşur.

### 1. 🎬 OpenCV (Görüntü ve Video İşleme)

Bu bölüm, OpenCV'nin hem durağan görüntüler hem de video akışları üzerindeki temel manipülasyon yeteneklerini gösterir.

#### Video İşleme Uygulamaları

| Dosya Adı | Açıklama | Anahtar Fonksiyonlar |
| :--- | :--- | :--- |
| `1_video_ice_aktarma.py` | Harici bir video dosyasını kare kare okuma, oynatma hızını ayarlama (`time.sleep`) ve video özelliklerini sorgulama. | `cv2.VideoCapture()`, `cap.read()`, `cap.get()` |
| `2_video_acma_ve_video_kaydı.py` | Bilgisayar kamerasından canlı görüntü alıp (`cv2.VideoCapture(0)`), bu akışı belirlenen codec ile yeni bir dosyaya **kaydetme**. | `cv2.VideoWriter()`, `cv2.VideoWriter_fourcc` |

#### Görüntü İşleme Uygulamaları

| Dosya Adı | Açıklama | Anahtar Fonksiyonlar |
| :--- | :--- | :--- |
| `1_resmi_ice_aktarma.py` | Bir resmi okuma, görüntüleme ve gri tonlamalı olarak kaydetme. | `cv2.imread()`, `cv2.imshow()`, `cv2.imwrite()` |
| `2_yeniden_boyutlandırma_ve_kırpma.py` | Resimleri yeniden boyutlandırma (`cv2.resize`) ve piksel koordinatları kullanarak kırpma. | `img.shape`, `cv2.resize()` |
| `3_sekiller_ve_metin.py` | Siyah bir tuval üzerine temel geometrik şekiller (çizgi, dikdörtgen, çember) çizme ve metin ekleme. | `cv2.line()`, `cv2.rectangle()`, `cv2.putText()` |
| `5_perspektif_.py` | Bir resmin (örn. bir kart) düz bir görünümünü elde etmek için **perspektif dönüşümü** uygulama. | `cv2.getPerspectiveTransform()`, `cv2.warpPerspective()` |
| `6_goruntuleri_karistirmak.py` | İki resmi farklı ağırlıklarla karıştırarak yeni bir görüntü oluşturma (`blending`). | `cv2.addWeighted()`, `cv2.cvtColor()` |
| `7_goruntu_esikleme.py` | Görüntüleri ikili hale getirmek için **Global** ve **Adaptif Eşikleme** yöntemleri. | `cv2.threshold()`, `cv2.adaptiveThreshold()` |

---

### 2. 📊 NumPy ve Pandas (Veri Manipülasyonu)

Görüntü ve bilimsel veri işleme için temel veri yapıları ve analitik işlemleri.

| Dosya Adı | Kütüphane | Açıklama |
| :--- | :--- | :--- |
| `numpyKutuphanesi.py` | **NumPy** | Matrisler ve dizilerle temel matematiksel işlemler, yeniden şekillendirme, rastgele sayı üretme ve indeksleme (`slicing`) teknikleri. |
| `pandasKutuphanesi.py` | **Pandas** | Veri analizi için **DataFrame** oluşturma, veri özetleme, satır/sütun seçimi (`loc`, `iloc`), **filtreleme** ve birleştirme (`pd.concat`). |

---

### 3. 📈 Matplotlib ve OS (Görselleştirme ve Sistem)

| Dosya Adı | Kütüphane | Açıklama |
| :--- | :--- | :--- |
| `MatplotlibKutuphanesi.py` | **Matplotlib** | Sayısal verileri çizgi ve dağılım grafikleriyle görselleştirme, alt grafikler (`plt.subplots`) oluşturma ve rastgele matrisi resim olarak gösterme. |
| `OS_Kutuphanesi.py` | **OS** | İşletim sistemi ile ilgili temel işlemler: Klasörde dolaşma (`os.chdir`), klasör oluşturma/silme (`os.mkdir`, `os.rmdir`) ve dosya listeleme (`os.listdir()`). |

---







