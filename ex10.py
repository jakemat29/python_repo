from sys import argv
script, user_name = argv
prompt = "#"
print "hi %s this is script %s" %(user_name, script)
print "what is ur name",
name = raw_input(prompt)
print "where do you live",
addr = raw_input(prompt)
print "hi %s with user name %s .you live in %s " %(name, user_name, addr)

