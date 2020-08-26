import cv2,os
from sklearn.externals import joblib
import numpy as np
import csv

import glob
label = "5"
dirList = glob.glob("orig_images/"+label+"/*.png")
for img_path in dirList:
	file_name = img_path.split("/")[2]
	print file_name	
	im = cv2.imread(img_path)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im_gray = cv2.GaussianBlur(im_gray, (15, 15), 0)
	roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)


	data=[]
	data.append(label)
	rows,cols = roi.shape

	for i in range(rows):
	    for j in range(cols):
	        k = roi[i,j]
	        if k>100:
	        	k=1
	        else:
	        	k=0	

	        data.append(k)

	with open('csv/dataset5labels.csv', 'ab') as f:
		writer = csv.writer(f)
		writer.writerow(data)
	
	cv2.waitKey()

