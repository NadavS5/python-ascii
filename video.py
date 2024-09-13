import numpy as np
import cv2 as cv
 
from PIL import Image
import sys
import time
import os


cap = cv.VideoCapture(0 )

if(len(sys.argv) > 1) :
    fname = sys.argv[1]
    cap = cv.VideoCapture(fname )

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height  = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

max_width = 300 # you can change it

ASPECT_RATIO = width/height 
resolution = width
if(max_width < width):
    resolution = width/ max_width #2 # 1 is highest around 2 is recommended

step_x = int(resolution)
step_y = int(ASPECT_RATIO * resolution)

brightness_map = [' ','.',',',':', ';','^', ']', 'A', 'K', 'G','$','░', '▒','■', '▓', '█']

def pixel_to_char(pixel):

    #convert to int because numpy array is 8 bit (capped at 256)
    index = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3
    #index is between 0 to 255
    index /=16
    #index is between 0 to 16
    
    return brightness_map[int(index)]

while cap.isOpened():
    ret, frame = cap.read()
    
    
    


    
    
    
    #os.system('cls')
    print("\033[%d;%dH" % (0, 0)) #reset cursor position
    # y max is height
    # x max is width
    

    for y in range(0,height,step_y):
        final = ""
        
        for x in range(0,width,step_x ):
            char = pixel_to_char(frame[(y,x)])
            #print(char, end = "")
            final +=char
       
        #print()
        print(final)
        

cap.release()
cv.destroyAllWindows()

