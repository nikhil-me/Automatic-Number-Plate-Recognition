from PIL import Image
import math
 
 
def sobel(img):
    if img.mode != "RGB":
        img = img.convert("RGB")
 
    out_img = Image.new("L", img.size, None)
    img_data = img.load()
    out_data = out_img.load()
 
    # convolution matrices
    matrix_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    matrix_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    matrix_size = 3
    matrix_middle = matrix_size/2
 
    rows, cols = img.size
 
    for row in xrange(rows-matrix_size):
        for col in xrange(cols-matrix_size):
            # each matrix placement
 
            pixel_x = 0
            pixel_y = 0
            for i in xrange(matrix_size):
                for j in xrange(matrix_size):
                    # each position in the convolution matrix
 
                    # find average pixel colour (discard colour info)
                    # of pixel at matrix overlap position
                    val = sum(img_data[row+i,col+j])/3
                    # apply convolution matrix multiplier
                    # to this value
                    pixel_x += matrix_x[i][j] * val
                    pixel_y += matrix_y[i][j] * val
 
            # place this new pixel in the middle of the convolution matrix
            new_pixel = math.sqrt(pixel_x * pixel_x + pixel_y * pixel_y)
            new_pixel = int(new_pixel)
            out_data[row+matrix_middle,col+matrix_middle] = new_pixel
 
    return out_img
