#Samuel DeLaughter
#12/3/14

#A simple pseudo-proof of the Collatz conjecture
#Accepts minimum and maximum values as optional arguments

import sys

MIN=1
MAX=10
if len(sys.argv) == 3:
	MIN = int(sys.argv[1])
	if MIN < 1:
		MIN = 1
	MAX = int(sys.argv[2])
	if MAX < MIN:
		MAX=MIN+1

def test(number):
	n = number
	counter = 0
	while not (n == 1):
		if n % 2 == 0:
			n = (n / 2)
		else:
			n = ((n * 3) + 1)
		counter+=1
	print ('Reached 1 from ' + str(number) + ' in ' + str(counter) +  ' steps')

def main():
	number=MIN
	while number <= MAX:
		test(number)
		number+=1
	print('Done')

if __name__ == '__main__':
    main()
