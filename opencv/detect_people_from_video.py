#!/usr/bin/env python
import cv2
import numpy as np
import sys, time
import itertools as it
from common import clock, draw_str

KEY_ECS = 27

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

def detect_people(img, hog):
    found, w = hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
    found_filtered = []
    for ri, r in enumerate(found):
        for qi, q in enumerate(found):
            if ri != qi and inside(r, q):
                break
        else:
            found_filtered.append(r)
            
    draw_detections(img, found)
    draw_detections(img, found_filtered, 3) 
    #print '%d (%d) found' % (len(found_filtered), len(found))       

def play_video(video_path):
    videoCapture = cv2.VideoCapture(video_path)
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    success, img = videoCapture.read()
    frame_count = 0
    time_start = clock()
    # Loop until there are no more frames.
    while success:
        
        detect_people(img, hog)
           
        time_span = clock() - time_start
        if time_span == 0:
            fps = 0
        else:
            fps = frame_count / time_span
            
        draw_str(img, (5,30), 'fps: %d' % fps)    
        cv2.imshow('video', img)
        if 0xFF & cv2.waitKey(5) == KEY_ECS:
            break
        success, img = videoCapture.read()
        frame_count += 1

    cv2.destroyAllWindows()

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'python read_video.py <video_path>'
		exit(0)

	video_path = sys.argv[1]  
	play_video(video_path)