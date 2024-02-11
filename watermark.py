# OpenCV is required to be installed
# use pip3 install opencv-python
import os
import cv2 
logo = cv2.imread("logo.png") 

def add_watermark(file) :
    print("Add watermark for file " + file)
    img = cv2.imread(file)
    h_logo, w_logo, _ = logo.shape  
    h_img, w_img, _ = img.shape
    
    top_y = int(h_img - h_logo - 10) 
    bottom_y = top_y + h_logo
    left_x = int(w_img - w_logo - 10)
    right_x = left_x + w_logo
 
    watermarked = img[top_y:bottom_y, left_x:right_x] 
    result = cv2.addWeighted(watermarked, 1, logo, 0.5, 0) 

    img[top_y:bottom_y, left_x:right_x] = result 
    cv2.imwrite("./watermarked/" + os.path.basename(file), img) 

for file in os.listdir("./photos"):
    add_watermark("./photos/" + file)