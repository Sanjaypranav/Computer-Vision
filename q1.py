"""
Read and Display open
perform image
resizing opencv
convert a colored image into grayscale
aafine , scaling , rotation, euclidien and similarity transformations
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def read(filename):
    img = cv2.imread(filename)
    # BGR to RGB conversion
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def read_as_grayscale(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    return img

def display(img, title: str = "Original Image"):
    plt.title(title)
    plt.imshow(img)
    plt.show()
    
    return img

def resize(img, size : tuple):
    return cv2.resize(img, size)

def affine(img):
    rows, cols = img.shape[:2]
    # Define the 3 pairs of corresponding points 
    input_pts = np.float32([[0,0], [cols-1,0], [0,rows-1]])
    output_pts = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
    M= cv2.getAffineTransform(input_pts , output_pts)
    return M

def rotate(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

def scale(img):
    return cv2.resize(img, None, fx=0.5, fy=0.5)

def euclidean(img):
    # warpaffine
    return cv2.warpAffine(img, affine(img), (img.shape[1] + 100,img.shape[0] + 100))

def flip(img):
    return cv2.flip(img, 1)

import cv2
  
# Function to extract frames
def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        success, image = vidObj.read()
        # Saves the frames with frame-count
        cv2.imwrite("computervision/frame/frame%d.jpg" % count, image)
  
        count += 1


if __name__ == "__main__":
    img = read("computervision/image/download.jfif")
    img_gray = read_as_grayscale("computervision/image/download.jfif")
    display(img)
    display(img_gray, "gray")
    display(resize(img, (100, 100)), "resized image")
    display(affine(img), "Affine")
    display(rotate(img), "rotate")
    display(scale(img), "scale")
    display(euclidean(img), "euclidean")
    display(flip(img), "flip")
    videopath = "computervision/video/video.mp4"
    FrameCapture(videopath)

