from PIL import Image
from pylab import *
from imtools import *

def set_gray_figure(img_array):
    figure()
    gray()
    imshow(img_array)
    axis('off')  
    
def set_histogram_figure(img_array, bin_num=128):
    figure()
    hist(img_array.flatten(),128)    

img_org = Image.open('./img/AquaTermi_lowcontrast.jpg')
img_color = array(img_org)
img_gray = array(img_org.convert('L'))

# img_arry = array(img_org)
# img_arry = imresize(img_arry, (50, 50))
# print img_arry.shape, img_arry.dtype

# img_arry = imresize(img_arry, (220, 220))

# box = (180, 180, 400, 400)
# img_partition = img_org.crop(box)
# img_partition = img_partition.resize((220,220))
#img_partition = img_partition.rotate(180)
# img_partition = img_partition.transpose(Image.ROTATE_180)

img_high_contrast, cdf = histeq(img_gray)

set_histogram_figure(img_color)
set_gray_figure(img_color)

set_histogram_figure(img_gray)
set_gray_figure(img_gray) 

set_histogram_figure(img_high_contrast)
set_gray_figure(img_high_contrast)

show()