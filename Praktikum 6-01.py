#flip gambar

#import
import numpy as np
import imageio
import matplotlib.pyplot as plt

#membaca gambar
img=imageio.imread("paris.jpg")

#mendaparkan resolusi dan type dari gambar
img_height=img.shape[0]
img_width=img.shape[1]
img_channel=img.shape[2]
img_type=img.dtype

#membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal=np.zeros(img.shape, img_type)
img_flip_vertical=np.zeros(img.shape, img_type)

#membalik gambar secara horizontal
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c]=img[y][img_width-1-x][c]

#membalik gambar secara vertical
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c]=img[img_height-1-y][x][c]

#menampilkan hasil balik gambar
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()