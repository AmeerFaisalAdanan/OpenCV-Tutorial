import cv2 as cv

# change res for existing video and images
def rescaleFrame(frame, scale=0.75):

    # set width and height of the image, convert to int
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    # resize the frame into the specified dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# work for live video only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)





# # Read video

# capture = cv.VideoCapture('Videos/dog.mp4') # use integer to capture from webcam/camera, pass file path if reading from video 

# while True:

#     #return boolean if the frame is successfully read |  read video frame by frame
#     isTrue, frame = capture.read()


#     frame_resized = rescaleFrame(frame, 0.5)
   

#     # display individual frame
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     # stopping frame
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# # release capture pointer from VideoCapture
# # destroy all opened windows
# cv.destroyAllWindows()


# cv.waitKey(0)