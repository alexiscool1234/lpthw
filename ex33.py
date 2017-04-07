def while_function(variable):
	i = 0
	numbers = []

	while i < variable:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i
		

	print "The numbers: "

	for num in numbers:
		print num

		

print "Please enter a number:"
variable = int(raw_input("> "))
while_function(variable)