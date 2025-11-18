"""
Operating System
Bilgisayar içerisindeki klasörlerde dolaşmayı sağlayan,
resimleri içeriye yüklerken, kayederken kullanılır. 
"""
import os

print(os.name) #os.nme -> hangi işletim sisteminde çalıştığını söyler

#hangi klasördeyim
currentDir = os.getcwd()
print(currentDir)

#new folder
folder_name = "new_folder"
os.mkdir(folder_name)

new_folder_name = "new_folder_2"
os.rename(folder_name, new_folder_name)

#farklı klasör içerisinde girme
#os.chdir(currentDir+"\\"+new_folder_name)
#print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

files = os.listdir()

for f in files:
    if f.endswith(".py"):
        print(f)
        
os.rmdir(new_folder_name)










