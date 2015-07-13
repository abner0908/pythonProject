from PIL import Image
from pylab import *
import random

# read image to array
im = array(Image.open('./img/success.jpg'))

# plot the image
imshow(im)

# some points
# x = [100,100,400,400]
# y = [200,500,200,500]
x = random.sample(range(500), 50)
y = random.sample(range(500), 50)

# plot the points with red star-markers
plot(x,y,'ro')

# line plot connecting the first two points
plot(x[:len(x)],y[:len(y)], 'r--')

# add title and show the plot
title('Plotting: "scuccess.jpg"')
show()