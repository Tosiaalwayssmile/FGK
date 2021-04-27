import os
import os.path
from vector import *

## Function parsing obj file
def read_obj_file(filename):
	vertices = []
	faces = []
	try:
		f = open(os.path.join(os.path.dirname(__file__) + "/OBJ", filename))
		for line in f:
			if line[0] == 'v' or line[0] == 'f':
				numbers = line[2:].replace('\n', '').split(' ')
				if line[0] == "v":
					vertices.append(Vec3(list(map(float, numbers))))
				elif line[0] == "f":
					ints = list(map(int, numbers))
					faces.append(Vec3([x - 1 for x in ints]))

		f.close()
		return vertices, faces
	except IOError:
		print(".obj file not found.")
