from PIL import Image
import sys
import time
import os

fname = sys.argv[1]

with Image.open(fname) as im:
    width, height = im.size
    px = im.load()



ASPECT_RATIO = width/height

max_width = 300

resolution = 1
if(max_width < width):
    
    resolution = width/ max_width #2 # 1 is highest around 2 is recommended

step_x = int(resolution)
step_y = int(ASPECT_RATIO * resolution  )



brightness_map = [' ','.',',',':', ';','*', 'r', '^', '0', 'A', 'm','F','M', 'K', 'O', 'Q']

def pixel_to_char(pixel):

    #convert to int because numpy array is 8 bit (capped at 256)
    index = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3
    #index is between 0 to 255
    index /=16
    #index is between 0 to 16
    print
    return brightness_map[int(index)]

start = time.time()

#os.system('cls')
for y in range(0,height,step_y):
    final = ""
    
    for x in range(0,width,step_x ):
        char = pixel_to_char(px[(x,y)])
        print(char, end="")
        #final +=char
    print('\n' ,end = "")
    
    #print(final)
    #final +='\n'



    #i timed printing every pixel 0.05, every line 0.035s ,and at the end of the frame 0.06
    #and at the end each line is the fastest 0.035s     
    
#print(final)

end = time.time()
print(end - start)

