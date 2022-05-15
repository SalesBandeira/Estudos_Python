import math

def circle_or_square(rad, area):
	square = (area **2) * 4
	pi = round(math.pi,2)
	circ = 2*pi*rad
	return circ > square 

print(circle_or_square(16, 625))    