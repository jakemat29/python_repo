def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r arg2: %r" %(arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r arg2: %r" %(arg1, arg2)

def mathcount(arg1, arg2):
	print "arg1 * arg2 = %d " %(arg1*arg2)
	
print_two("jake", "mat")
print_two_again("jacob", "mathew")	
mathcount(5,10)
print "enter the two no.s to perform the multiplication",
n1 = raw_input(">")
n2 = raw_input(">")
mathcount(int(n1), int(n2))
