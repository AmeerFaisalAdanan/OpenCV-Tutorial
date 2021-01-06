import cv2 as cv
import numpy as np 


# built in function to draw images are as following

# np.zeros((length, width, no_color_channel), dtype='uint8')
# pain black image using numpy
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# # paint color, in this case green color image
blank[200:300, 300:400] = 0,255,0 # color code is green
cv.imshow('Green', blank)

# drawing rectangle
# use blank as canvas, draw rectangle from origin (0,0) to (250,250) with green color (0,255, 0)
#  and set thickness by 2 pixel(or used cv.FILLED using)
# cv.rectangle(blank, (0,0), (250, 250), (0,255, 0), thickness=cv.FILLED)
# use blank as the canvas, from blank image, set the blank half
# draw using rectangle()
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)


# draw circle using circle()
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255, 0), thickness=cv.FILLED)
cv.imshow('Circle', blank)


# draw line line()
cv.line(blank, (100,250), (300, 400), (255,255, 255), thickness=3)
cv.imshow('Line', blank)


# write text on image putText()
cv.putText(blank, 'Hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,250,0), 2)
cv.imshow('Text', blank)


# img = cv.imread('../Photos/cat.jpg')
# cv.imshow('Cat', img)

cv.waitKey(0)