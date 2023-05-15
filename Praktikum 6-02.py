#inversi, transformasi logaritma, transformasi powerlaw

#import
import numpy as np
import imageio
import matplotlib.pyplot as plt

#membaca gambar
img=imageio.imread("paris.jpg")

img_height=img.shape[0]
img_width=img.shape[1]
img_channel=img.shape[2]


#inversi

#membuat variabel img_inversi
img_inversi=np.zeros(img.shape, dtype=np.uint8)

#membuat fungsi untuk inversi grayscale
def inversi_grayscale(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            gray=nilai-gray
            img_inversi[y][x]=(gray, gray, gray)

#membuat fungsi untuk inversi rgb
def inversi_rgb(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            red=nilai-red
            green=img[y][x][1]
            green=nilai-green
            blue=img[y][x][2]
            blue=nilai-blue
            img_inversi[y][x]=(red, green, blue)

#menampilkan hasil inversi
inversi_grayscale(255)
plt.imshow(img_inversi)
plt.title("Inversi Grayscale")
plt.show()

inversi_rgb(255)
plt.imshow(img_inversi)
plt.title("Inversi RGB")
plt.show()


#log

#membuat variabel img_log untuk menampung hasil
img_log=np.zeros(img.shape, dtype=np.uint8)

#mendefinisikan fungsi untuk log
def log(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue)) / 3
            gray=int(c*np.log(gray+1))
            if gray>255:
                gray=255
            if gray<0:
                gray=0
            img_log[y][x]=(gray, gray, gray)

#menampilkan hasil log
log(30)
plt.imshow(img_log)
plt.title("Log")
plt.show()


#invasi dan log

#membuat variabel img_inlog untuk menampung hasil
img_inlog=np.zeros(img.shape, dtype=np.uint8)

#mendefinisikan fungsi untuk inversi log
def inlog(c):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue)) / 3
            gray=int(c*np.log(255-gray+1))
            if gray>255:
                gray=255
            if gray<0:
                gray=0
            img_inlog[y][x]=(gray, gray, gray)

#menampilkan hasil inversi log
inlog(30)
plt.imshow(img_inlog)
plt.title("Inversi Log")
plt.show()


#nth root power

#membuat variabel img_nthrootpower
img_nthrootpower=np.zeros(img.shape, dtype=np.uint8)

#membuat fungsi untuk nth root power

def nthrootpower(c, y):
    thc = c / 100
    thy = y / 100
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(thc * pow(gray, 1./thy))
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_nthrootpower[y][x] = (gray, gray, gray)

#menampilkan hasil
nthrootpower(50, 100)
plt.imshow(img_nthrootpower)
plt.title("Nth Root Power")
plt.show()