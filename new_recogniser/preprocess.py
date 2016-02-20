from multiprocessing import Pool
from PIL import Image
import os
import os.path
import datasetresize

def get_images(path):
	subfolders=os.listdir(path)
	
	for folder in subfolders:
		print folder
		count=1
		count=datasetresize.process_fpath(path+"/"+folder,count,folder[0])

		
get_images("/home/amit/Documents/btp-master/final_train_digit_images")
