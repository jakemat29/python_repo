from sys import argv
from os.path import exists
script, from_file, to_file =argv
print "*"*100
print "copying %r to %r" %(from_file, to_file)
infile = open(from_file)
indata = infile.read()
print "the file to be copied is %d size" %len(indata)
print "does the output file exists? %r" %exists(to_file)
out_file = open(to_file, 'w')
out_file.write(indata)
infile.close()
