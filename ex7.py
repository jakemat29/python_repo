formatter = "%r %r %r %r"
print formatter %(1, 2, 3, 4)
print formatter %('one', 'two', 'three', 'four')
print formatter %(True, False, False, True)
print formatter % ('i would like' , 'to know something' , 'say Mr.Francis' , "please be Honest")
print formatter % (formatter, formatter,formatter, formatter)


print "*" * 100

days = "monday, tuesday, wednesday, thursday, friday, saturday, sunday"
months = " jan \n feb \n mar \n apr \n jun \n jul \n aug \n sep \n oct \n nov \n dec"
print days
print months

print "*" * 100

print """
	any no of lines 
	could be written if the 3 quotes are 
	used . just an illustration.
"""				# it should either be a double quote or double quote


print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string
print "\t I'm printed with a tab space"
print "this string \n is broken into 2 lines"
print "I'm \\ a \\ cat" # if '\' needed to be inside a string