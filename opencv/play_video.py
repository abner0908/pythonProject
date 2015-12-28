#!/usr/bin/env python
import cv2
import numpy as np
import sys

KEY_ECS = 27


def play_video(video_path):
    videoCapture = cv2.VideoCapture(video_path)
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

    success, img = videoCapture.read()
    # Loop until there are no more frames.
    while success:
        cv2.imshow('video', img)
        if 0xFF & cv2.waitKey(5) == KEY_ECS:
            break
        success, img = videoCapture.read()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'python read_video.py <video_path>'
        exit(0)

    video_path = sys.argv[1]
    play_video(video_path)
