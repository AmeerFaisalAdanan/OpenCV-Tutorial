import cv2 as cv

img = cv.imread('./Photos/cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# blurring image
# cv.GaussianBlur(sourceImage, (kernel size))
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) 
cv.imshow('Blur', blur)


cv.waitKey(0)