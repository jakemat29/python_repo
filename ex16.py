def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
	quo = a/b
	mod = a%b
	return quo, mod

sum = add(5,10)
min = subtract(45, 40)
prod = multiply(20, 10)
div, modulus = divide(26,5)
print "sum = %d minus = %d product = %d  division = %d modulus = %d" %(sum, min, prod, div, modulus)	  