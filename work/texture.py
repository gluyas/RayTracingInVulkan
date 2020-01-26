from PIL import Image
import numpy as np
import pywavefront as wav

global textures


def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data


def save_image( npdata, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "RGB" )
    img.save( outfilename )


def equal ( arr1, arr2 ) :
	if len(arr1) != len(arr2):
		return False

	for i in range(len(arr1)):
		if arr1[i] != arr2[i]:
			return False

	return True


def avg_arrays ( arr1, arr2 ) :
	if len(arr1) != len(arr2):
		return arr1

	arr = [0 for i in range(len(arr1))]
	for i in range(len(arr1)):
		arr[i] = (arr1[i] + arr2[i]) / 2

	return arr


def get_colour( uv, mat ) :
	if mat == 0:
		return (0, 0, 0)
	else:
		tex = textures[mat-1]
		rows = len(tex)-1
		cols = len(tex[0])-1

		i = int(round(uv[1] * rows, 0))
		j = int(round(uv[0] * cols, 0))

		return tex[i][j]


def get_points( scene ) :
	points = []

	m = 0
	for material in scene.mesh_list[0].materials:
		index = 0

		while index < len(material.vertices):
			u = material.vertices[index]
			v = material.vertices[index+1]
			x = material.vertices[index+8]
			y = material.vertices[index+9]
			z = material.vertices[index+10]
			c = get_colour((u,v), m)

			points.append(((u, v), (x, y, z), c))

			index += 11

		m += 1

	return points


def generate_image( data ) :
	n = 1000
	img = [[[0,0,0] for x in range(n)] for y in range(n)]

	for point in data:
		uv = point[0]
		c = point[2]

		i = int(round(uv[1] * (n-1), 0))
		j = int(round(uv[0] * (n-1), 0))

		if False == equal(img[i][j], [0, 0, 0]):
			img[i][j] = avg_arrays(img[i][j], [c[0], c[1], c[2]])
		else:
			img[i][j] = [c[0], c[1], c[2]]

	return img


if __name__ == '__main__':
	alex1 = load_image("img/Alex1.jpg")
	alex2 = load_image("img/Alex2.jpg")
	alex3 = load_image("img/Alex3.jpg")
	textures = [alex1, alex2, alex3]

	origAlex = wav.Wavefront('img/models/Alex.obj')
	#uvMappedAlex = origAlex

	print("loaded successfully :)")

	origPoints = get_points(origAlex)
	#newPoints = get_points(uvMappedAlex)

	final = generate_image(origPoints)
	save_image(final, "combined.jpg")
