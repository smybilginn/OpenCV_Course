import cv2
import matplotlib.pyplot as plt

# blending
img1 = cv2.imread("img1.jpg")
img1= cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) #OpenCV’nin BGR’sini matplotlib’in RGB formatına çeviriyor, böylece renkler doğru görünür.
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape) #Resmin yükseklik, genişlik, kanal sayısı bilgisini verir.
print(img2.shape)

img1 = cv2.resize(img1,(600,600)) #Resmi istediğin boyuta getirir.
print(img1.shape)

img2 = cv2.resize(img2,(600,600)) #Her iki resmi 600x600 yaptık, böylece boyutlar aynı oldu.
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# blended = alpha*img1 + beta*img2 + gamma
blended = cv2.addWeighted(src1=img1, alpha = 0.3, src2=img2,beta=0.7, gamma = 0)
plt.figure()
plt.imshow(blended)

"""
İki resmi okuduk ve renkleri RGB’ye çevirdik.

İlk boyutları kontrol ettik, gerekirse yeniden boyutlandırdık.

Matplotlib ile ayrı pencerelerde görüntüledik.

addWeighted ile resimleri alpha ve beta ağırlıklarıyla birleştirdik.
"""







