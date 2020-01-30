from PIL import Image
import numpy as np
from math import *

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data


def save_image( data, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(data,0,255), dtype="uint8"), "RGB" )
    img.save( outfilename )
	
def create_array( data, rows ) :
	ar = ceil(np.sqrt(rows))
	return [[[0,0,0] for x in range(ar)] for y in range(ar)]
			
	
def create_image( file ) :
	temp = np.genfromtxt(file, delimiter = ',')
	img = Image.fromarray( temp, 'RGB' )
	
	cols, rows = img.size
	arr = create_array(temp, rows)
	
	for row in range(len(arr)):
		for col in range(len(arr)):
			index = (row * len(arr)) + col
			if index < rows:
				arr[row][col] = temp[index]
		
	save_image(arr, "../textures/Data_rgb.jpg")
	

if __name__ == '__main__':
	csv_file = open('Data_rgb.csv', 'r')
	create_image(csv_file)