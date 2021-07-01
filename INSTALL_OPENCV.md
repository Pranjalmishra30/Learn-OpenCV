## Install OpenCV  
OpenCV is an open source computer vision and machine learning software library.  
**Note**: Ensure that the latest version of [python3](https://www.python.org/downloads/) is installed on your system.  


## Linux  
All the commands written below should be executed in the terminal.  
**Note:** ~$ is not part of the command  

1. If pip is not installed, then   
    
    ```
    ~$ sudo apt-get install python3-pip  
    ```
    We require pip3 for python3 and we will be using pip3 for all other libraries. Refer [here](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) for more info.  
    **Note**: To check your pip3 version  
    
    ```
    ~$ pip3 --version  
    ```
2. Installing scikit-build (required for OpenCV Package)

    ```
    ~$ pip3 install scikit-build
    ```

3. Installing OpenCV  
    ```
    ~$ pip3 install opencv-python
    ```

    Wait for the packages to download and install.  

## Windows and MacOS  
Open command prompt (on windows) or terminal (on macOS) and run the following command.  

1. Installing OpenCV  
    ```
    pip install opencv-python
    ```  
    Wait for the packages to download and install.    

### Verifying your installation:  
Run this python code in your terminal or IDE to make sure that the CV2 library is installed.  
```
import cv2
#Simple Video capture from webcam

cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

## References  
* [Official website](https://opencv.org/)  
* [Installation instructions](https://pypi.org/project/opencv-python/)
