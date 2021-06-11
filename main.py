# largest number
# create a function
def largest_number():
	x=[5,6,7]
	y=1
	for z in x:
		if y<z:
			y=z
	print("largest_number=",z)
# call function
largest_number()
# lowest number 
# create a function 
def lowest_number():
	x=[1,2,3]
	low=4
	for y in x:
		if low>y:
			low=y
	print("lowest_number=",low)
# call a function   
lowest_number()

