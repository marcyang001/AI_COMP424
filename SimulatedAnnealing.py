
import math
import numpy as np
import operator
from pprint import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
import random

"""
x has the type double
assume the input x to sin((x^2)/2) is in radians

"""

def evaluation(x):
	
	try:
		y = math.sin(math.pow(x, 2)/2.0)/math.sqrt(x)
		return y
	except ZeroDivisionError:
		return 0

"""
find the temporary max from the starting point to the end point

by hill climing method

"""

def HillClimbing(startPoint, endPoint, stepSize):

	drange = np.arange(startPoint, endPoint+stepSize, stepSize)
	temp_max = evaluation(drange[0])
	num_steps = 0
	x_val = 0
	#print drange
	for ind, val in enumerate(drange):
		
		if temp_max > evaluation(val):
			num_steps = ind
			x_val = val
			break
		else:
			temp_max = evaluation(val)
	

	return startPoint, num_steps, temp_max



"""
generate starting point, step number, max_y 

for every starting points in (0, 10]

"""

def generatePointsHC(startPoint, endPoint, stepSize):

	points = []
	for i in range(startPoint, endPoint):
		points.append(HillClimbing(i, endPoint, stepSize))

	return points


"""
Plot the 3D graph with given points (x, y, z)  

"""
def plotGraph(points, xlabel, ylabel, zlabel):
	x_val = [x[0] for x in points]
	y_val = [y[1] for y in points]
	z_val = [z[2] for z in points]

	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.set_zlabel(zlabel)
	ax.plot(x_val, y_val, z_val)
	plt.show()

"""
Acceptance probability is e^((new cost - old cost)/T)

"""
def acceptance_probability(deltaE, T):
	a = math.exp(deltaE/T)

	return a

"""

Simulated annealing algorithm:

temperature cooling concept is referenced from: 
www.cs.nott.ac.uk/~pszgxk/aim/notes/simulatedannealing.doc

I used T = T * alpha 

where 0.8 <= alpha <= 0.99 for the best result 


"""
def Simulated_Annealing(startPoint, endPoint, stepSize, T, alpha):

	#all the possible range from start point to endpoint
	drange = np.arange(startPoint, endPoint+stepSize, stepSize)

	current_val = evaluation(startPoint)
	

	T_min = 0.000001

	#print 
	stepNumber = 0
	while T > T_min:
		
		#randomly select the new neighbor
		new_neighbour = drange[random.randint(0, len(drange)-1)]
		next_value = evaluation(new_neighbour)
		deltaE = next_value - current_val
		
		#accept the value if the new neighbor is bigger 
		if deltaE > 0:
			current_val = next_value
		
		else:
			#accept the bad moves with probability e^(deltaE/T)
			ap = acceptance_probability(deltaE, T)
			if ap > random.random():
				current_val = next_value
			T = T * alpha

		stepNumber = stepNumber + 1
		#temperature cooling
		
		
	return startPoint, stepNumber, current_val




def generatePointsSA(startPoint, endPoint, stepSize, T, alpha):

	points = []
	for i in range(startPoint, endPoint):
		points.append(Simulated_Annealing(i, endPoint, stepSize, T, alpha))

	return points

pointsForSA = generatePointsSA(0, 10, 0.01, 1.0, 0.9)

pointsForHC = generatePointsHC(0, 10, 0.01)
#pprint(pointsForHillClimbing)

xlabel = "Starting Point"
ylabel = "number of steps"
zlabel = "local y-max"

names = (xlabel, ylabel, zlabel)


print "\nPoints generated from Hill Climbing Algorithm\n"
for points in pointsForHC:
	print points[0],",", points[1],",",points[2]

#plotGraph(pointsForHC, xlabel, ylabel, zlabel)

print "\nPoints generated from simulated annealing\n"
for points in pointsForSA:
	print points[0],",", points[1],",",points[2]

#plotGraph(pointsForSA, xlabel, ylabel, zlabel)



