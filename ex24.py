import pdb
def add(a, b):
	print "this method add 2 nos"
	return a + b
print "1st line"
pdb.set_trace()
a = 5 
b = 12
c = add(a,b)
print "sum = %d" %c
print "2nd line"
print "3rd line"