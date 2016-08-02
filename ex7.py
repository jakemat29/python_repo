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