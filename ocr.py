import sys
import pafy
import numpy as np
import os
import cv2
import imageio
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
inp = input().split("--")
url = inp[0]
videoPafy = pafy.new(url)
video_exists = False
frame_exists = False
timeStamp = int(inp[1])
time_length = videoPafy.length
fps = 30
frame_seq = (timeStamp*fps)*100
frame_no = (timeStamp/time_length)
# for local /home/kowdinya/Documents/ytCoderServer
for file in os.listdir("/"):
    if(file == "frame"  + str(timeStamp) + videoPafy.title  + ".jpg"):
        frame_exists = True
        video_exists = True
        print('frame exists')
        break
    if(file == videoPafy.title + ".mp4"):
        video_exists = True
        print('video exists')
streams = videoPafy.streams  
if(video_exists == False):
    best = videoPafy.getbest()
    best.download()
if(frame_exists == False):
    ffmpeg_extract_subclip(videoPafy.title + ".mp4", timeStamp, timeStamp + 1, targetname="cut_" + str(timeStamp) + videoPafy.title  + ".mp4")
    cap =  cv2.VideoCapture("cut_" + str(timeStamp) + videoPafy.title  + ".mp4")
    frame = 0
    frame_seq = 30
    success,image = cap.read()
    success = True
    while success:
        if(frame/frame_seq == 1):
             cv2.imwrite("frame"  + str(timeStamp) + videoPafy.title  + ".jpg", image)
             break
        success,image = cap.read()
        frame += fps
    cap.release()
    cv2.destroyAllWindows()
from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
demo = Image.open("frame"  + str(timeStamp) + videoPafy.title  + ".jpg")
text = pytesseract.image_to_string(demo,lang='eng')
print(text)