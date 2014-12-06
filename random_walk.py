# Samuel DeLaughter
# 12/6/14

#This program graphs the probability of landing on each integer in a given interval for a 1D random-walk simulation
#If called with a -i flag, it will prompt for user input on the following variables:
	#Boundary numbers, starting position, number of steps per simulation, number of simulations

import sys
import random
import numpy as np
import matplotlib.pyplot as plt

#Set default values for the variables
MIN_POSITION = -10
MAX_POSITION = 10
START_POSITION = 0
NSTEPS = 12
NSIMS = 1000

if('-i' in sys.argv):
#Get user input for variables if called with the -i argument
	MIN_POSITION = int(raw_input("Enter lower boundary: ") or MIN_POSITION)
	MAX_POSITION = int(raw_input("Enter upper boundary: ") or MAX_POSITION)
	
	#If the upper boundary is smaller than the lower boundary, swap them
	sorted_bounds = sorted((MIN_POSITION, MAX_POSITION))
	MIN_POSITION = sorted_bounds[0]
	MAX_POSITION = sorted_bounds[1]
	
	#If the two boundaries are equivalent, increment the upper bound
	if(MIN_POSITION == MAX_POSITION):
		MAX_POSITION+=1
	
	START_POSITION = int(raw_input("Enter starting position: ") or START_POSITION)
	#Make sure the starting position is within the min/max bounds
	
	START_POSITION=sorted((MIN_POSITION, START_POSITION, MAX_POSITION))[1]
	
	NSTEPS = int(raw_input("Enter number of steps for each simulation: ") or NSTEPS)
	NSIMS = int(raw_input("Enter number of simulations to run: ") or NSIMS)
		

def move(position):
#Change the current position
	if(position == MAX_POSITION):
		#If you're at the upper boundary, either stay put or decrease
		step=random.randint(-1, 0)
	elif(position == MIN_POSITION):
		#If you're at the lower boundary, either stay put or increase
		step=random.randint(0, 1)
	else:
		#If you're within the boundaries, either stay put, decrease, or increase
		step=random.randint(-1, 1)
	position += step
	return position
	
	
def sim():
#Run a simulation
	position=START_POSITION
	for i in range(NSTEPS):
		position=move(position)
	return position


def main():
	results=[]
	for i in range(NSIMS):
		results.append(sim())
	counts=[]
	for i in range(MIN_POSITION, (MAX_POSITION+1)):
		counts.append(results.count(i))
		
	plt.plot(range(MIN_POSITION, (MAX_POSITION+1)), counts, 'ro')
	#Set axis intervals
	plt.xticks(np.arange(MIN_POSITION, (MAX_POSITION + 1), 1.0))
	#plt.yticks(np.arange(0, max(counts), 100))
	#Display gridlines
	plt.grid(b=True, which=u'major', axis=u'both')
	plt.show()
	
	#Make the plot window visible
	wm = plt.get_current_fig_manager() 
	wm.window.attributes('-topmost', 0)


if __name__ == '__main__':
    main()
