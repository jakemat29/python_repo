def start():
	print "It is very dark..\n You can see 2 Doors.... \n which one do you choose left or right"
	door_sel = raw_input(">>")
	if door_sel == "left":
		bear_room()
	elif door_sel == "right":
		lion_room()
	else:
		print "you starve to death you moron........."
def dead(why):
	print why
	exit(0)
	
def bear_room():
	print "The bear is taking honey...\n you have 2 ways of exit ....\n"
	print "take honey "
	print "taunt bear"
	print "open door"
	bear_moved = False
	while True:
		choice = raw_input(">>")
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			print "The bear has moved from the door. You can go through it now."
			
			
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
start()		