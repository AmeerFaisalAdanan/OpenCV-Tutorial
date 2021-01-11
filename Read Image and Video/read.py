import cv2 as cv


# # image part 

# img = cv.imread('Photos/cat.jpg') # read images from Photo directory that contain cat.jpg

# cv.imshow('Cat', img) #show images in new windows called Cat

# cv.waitKey(0) # wait for keypress or close window


# Read video

capture = cv.VideoCapture('Videos/dog.mp4') # use integer to capture from webcam/camera, pass file path if reading from video 

while True:

    #return boolean if the frame is successfully read |  read video frame by frame
    isTrue, frame = capture.read()

    # display individual frame
    cv.imshow('Video', frame)

    # stopping frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release capture pointer from VideoCapture
# destroy all opened windows
cv.destroyAllWindows()


# -215:Assertion failed will be throw when all the frame has been viewed in the video or whe 