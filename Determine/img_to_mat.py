import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
import PIL
from PIL import Image
import numpy as np

#first convert the image binary scale
#using function im.convert('L')

#converting image to intensity matrix
img=mpimg.imread('img.bmp')
#print img

#find the first pixel from top black color

for i in range(1,img.size[1]):
	print img[0,i]+" "
