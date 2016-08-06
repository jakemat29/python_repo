def start():
	print "It is very dark..\n You can see 2 Doors.... \n which one do you choose left or right"
	door_sel = raw_input(">>")
	if door_sel == "left":
		bear_room()
	elif door_sel == "right":
		lion_room()
	else:
		print "you starve to death you moron"
start()		