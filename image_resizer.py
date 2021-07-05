import cv2
import os

for filename in os.listdir("experiment data"):
    for image_name in os.listdir("experiment data/" + filename + "/images/"):
        image_dir = "experiment data/" + filename + "/images/" + image_name
        img = cv2.imread(image_dir)
        img = cv2.resize(img,(0,0),fx = 0.4, fy = 0.4)
        cv2.imwrite(image_dir,img)