from sys import argv

script, filename = argv

print "we are opening file %r" %filename
target = open(filename, 'a')     #here the file is opened in append mode... 
			#if it is in write mode itll overwrite the contents ofnthe file
#target.truncate()

print "enter 3 lines of text"
line1 = raw_input(" line1: ")
line2 = raw_input("Line2:")
line3 = raw_input("Line3:")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
