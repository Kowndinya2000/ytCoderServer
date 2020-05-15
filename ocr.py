print('Hello from main')
import sys

print(input())
url = "https://www.youtube.com/watch?v=W1e5wO7XR2w"
timeStamp = 55
time_length = 743.0
print(time_length)
print(timeStamp)

fps = 30
frame_seq = (timeStamp*fps)*100
frame_no = (timeStamp/time_length)
print(frame_no)
print(frame_seq)
import pafy
import numpy as np
videoPafy = pafy.new(url)
import os
bool_flag = False
for root, dirs, files in os.walk("/"):
        for file in files:
            if(file == videoPafy.title + ".mp4"):
                print('File exists')
                bool_flag = True
                break 
streams = videoPafy.streams 
for i in streams: 
    print(i) 
if(bool_flag == False):
    best = videoPafy.getbest()
    print(best.resolution, best.extension) 
    print(best)
    best.download()
import cv2
# 
# cap.set(2,frame_no)
# ret, frame = cap.read()
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# my_video_name = best.url.split(".")[0]
# cv2.imshow(my_video_name + "frame "+ str(frame_seq),gray)
# cv2.waitKey()
# cv2.imwrite(my_video_name+"_frame_"+str(frame_seq)+'.jpg',gray)
import imageio
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip(videoPafy.title + ".mp4", timeStamp, timeStamp + 1, targetname="cut.mp4")
cap =  cv2.VideoCapture("cut.mp4")
frame = 0
frame_seq = 30
success,image = cap.read()
success = True
while success:
    if(frame/frame_seq == 1):
         cv2.imwrite("frame.jpg", image)     # save frame as JPEG file
         break
    success,image = cap.read()
    frame += fps
cap.release()
cv2.destroyAllWindows()
print('Image creation Success!')
from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
demo = Image.open("frame.jpg")
text = pytesseract.image_to_string(demo,lang='eng')
print(text)
















# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# def remove_noise(image):
#     return cv2.medianBlur(image,5)
# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# def dilate(image):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.dilate(image,kernel,iterations=1)
# def erode(image):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.erode(image, kernel, iterations = 1)

# #opening - erosion followed by dilation
# def opening(image):
#     kernel = np.ones((5,5),np.uint8)
#     return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# #canny edge detection
# def canny(image):
#     return cv2.Canny(image, 100, 200)

# #skew correction
# def deskew(image):
#     coords = np.column_stack(np.where(image > 0))
#     angle = cv2.minAreaRect(coords)[-1]
#     if (angle < -45):
#         angle = -(90 + angle)
#     else:
#         angle = -angle
#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#     return rotated

# #template matching
# def match_template(image, template):
#     return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)    

# gray = get_grayscale(img)
# thresh = thresholding(img)
# opening = opening(gray)
# canny = canny(gray)