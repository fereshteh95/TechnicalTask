import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import argparse
start_time = time.time()


my_parser = argparse.ArgumentParser()
my_parser.add_argument('--img', action='store', type=str, required=True)
my_parser.add_argument('--query', action='store', type=str, required=True)

args = my_parser.parse_args()

img_path = args.img
temp_path = args.query

if not os.path.isfile(img_path):
    print('The path specified for the image does not exist')
    sys.exit()
if not os.path.isfile(temp_path):
    print('The path specified for the query does not exist')
    sys.exit()
    

img = cv2.imread(img_path, 0)
color_img = cv2.imread(img_path)
template = cv2.imread(temp_path,0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(color_img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)

# cv2.rectangle(color_img,top_left, bottom_right, (0, 0, 255), 2)

print("--- %s ms ---" % (round((time.time() - start_time)*1000, 2)))
print("Press any Key to Exit")
cv2.imshow("Image", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()