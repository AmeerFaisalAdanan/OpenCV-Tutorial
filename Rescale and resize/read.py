import cv2 as cv
import rescale as rs

# Read video

capture = cv.VideoCapture('../Videos/dog.mp4') # use integer to capture from webcam/camera, pass file path if reading from video 

while True:

    #return boolean if the frame is successfully read |  read video frame by frame
    isTrue, frame = capture.read()

    frame_resized = rs.rescaleFrame(frame, 0.5)
    

    # display individual frame
    # cv.imshow('Video', frame)

    cv.imshow('Video Resized', frame_resized)

    # stopping frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# release capture pointer from VideoCapture
# destroy all opened windows
cv.destroyAllWindows()
