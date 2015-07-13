from PIL import Image
from pylab import *
from imtools import *


img = Image.open('./img/lena_std.tif')
img_gray = img.convert('L')

# img_arry = array(img)
# img_arry = imresize(img_arry, (50, 50))
# print img_arry.shape, img_arry.dtype


img_arry = array(img_gray, 'f')
# img_arry = imresize(img_arry, (220, 220))
print img_arry.shape, img_arry.dtype

# box = (180, 180, 400, 400)
# img_partition = img.crop(box)
# img_partition = img_partition.resize((220,220))
#img_partition = img_partition.rotate(180)
# img_partition = img_partition.transpose(Image.ROTATE_180)
figure()
gray()
imshow(img_arry)

axis('off')

show()