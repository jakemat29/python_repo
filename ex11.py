from sys import argv
script, filename = argv
txt = open(filename)
print "here is ur file name %s" %filename
print txt.read() 
print "*" * 100

print "please enter gthe filename: ",
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
