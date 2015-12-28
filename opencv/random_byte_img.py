#!/usr/bin/env python

import cv2
import os
import time
import numpy

def create_rand_image():
	# Make an array of 120,000 random bytes.
	randomByteArray = bytearray(os.urandom(480000))

	flatNumpyArray = numpy.array(randomByteArray)

	# Convert the array to make a 400x100 color image.
	bgrImage = flatNumpyArray.reshape(400, 400, 3)
	cv2.imshow('Random Color Image', bgrImage)
	cv2.waitKey(3)

if __name__ == '__main__':
	while True:
		create_rand_image()
		time.sleep(1)
	
	cv2.destroyAllWindows()    		