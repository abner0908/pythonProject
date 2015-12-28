import cv2
from PIL import Image
from numpy import *
from pylab import *
from imtools import *

if __name__ == '__main__':
    file_path = './img/coca.jpg'
    im = cv2.imread(file_path)
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #im = cv2.equalizeHist(im)
    #im = array(Image.open(file_path).convert('L'))
    print im.shape
    #im = switchBR(im)

    #im = mirror_image(im)
    #im = 255 - im
    #show_image(im, method='PyLab')
    #figure('test')
    #imshow(im)
    #show()

    #print im
    #print type(im)
    show_image(im)
