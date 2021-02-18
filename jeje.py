import random

random.seed(1)
 #generate some Gaussian values
for _ in range(2):
	value = random.gauss(0, 1)
	print(value) 