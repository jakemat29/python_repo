i = 7
numbers = []
while(i < 12):
	print "the value of i now is %d \n" %i
	numbers.append(i)
	i = i + 1

print "*" * 100	

print "The numbers list follows"
for i in numbers:
	print "\n %d" %i
	