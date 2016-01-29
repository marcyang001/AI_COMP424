
import math
import numpy as np
import operator
from pprint import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""
x has the type double
assume the input x to sin((x^2)/2) is in radians

"""

def evaluation(x):
	y = math.sin(math.pow(x, 2)/2.0)/math.sqrt(x)
	return y

"""
find the temporary max from the starting point to the end point

by hill climing method

"""

def HillClimbing(startPoint, endPoint, stepSize):

	if startPoint == 0:
		startPoint = startPoint + stepSize

	drange = np.arange(startPoint, endPoint+stepSize, stepSize)
	temp_max = evaluation(drange[0])
	print drange
	num_steps = 0
	x_val = 0
	for ind, val in enumerate(drange):
		#print val
		if temp_max > evaluation(val):
			num_steps = ind
			x_val = val
			break
		else:
			temp_max = evaluation(val)
	

	return x_val, temp_max, num_steps



"""
generate max_x, max_y, stepnumber 

for every starting points in (0, 10]

"""

def generatePoints(startPoint, endPoint, stepSize):

	points = []
	for i in range(startPoint, endPoint):
		points.append(HillClimbing(i, endPoint, stepSize))


	return points


pointsForHillClimbing = generatePoints(0, 10, 0.01)


def generateGraph(points):
	x_val = [x[0] for x in points]
	y_val = [y[1] for y in points]
	z_val = [z[2] for z in points]

	ax.set_xlabel('x values')
	ax.set_ylabel('temp y_max')
	ax.set_zlabel('step number')
	ax.plot(x_val, y_val, z_val)
	plt.show()










