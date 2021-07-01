## Install OpenCV  
OpenCV is an open source computer vision and machine learning software library.  
**Note**: Ensure that the latest version of [python](https://www.python.org/downloads/) is installed on your system.  


## Linux  
All the commands written below should be executed in the terminal.  
**Note:** ~$ is not part of the command  

1. If pip is not installed, then   
    
    ```
    ~$ sudo apt-get install python3-pip  
    ```

    **Note**:  We require pip for python3 and we will be using pip3 for all other libraries. Refer [here](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/) for more info 

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
Run the python console in your system and import the libraries as shown below  
    
        ~$ python3  
	    >>> import cv2  

If this runs without any error, then your installation is successful.


## References  
* Official [website](https://opencv.org/)  
* Installation [instructions](https://pypi.org/project/opencv-python/)
