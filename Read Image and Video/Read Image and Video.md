#### Read image and video 

With OpenCV, you can read images and video



##### To read images 

``` cv.imread() ```
opencv support reading various image extensions such as jpg, png, tiff etc

##### To view images 
``` cv.imshow() ```

``` imshow ``` to display the image we have load earlier


##### To read video 

``` cv.VideoCapture('videofile') ```

opencv support reading various video extension such as mp4, avi etc


##### To view the video

``` 
    #return boolean if the frame is successfull read |  read video frame by frame
    isTrue, frame = capture.read()

    # display individual frame
    cv.imshow('Video', frame)

    # stopping frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
```


To test the code, run ```python read.py```. Try to uncomment the image part to view how to read and view the image using OpenCV

