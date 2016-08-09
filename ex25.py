player_data = [{"name":"mingolet", "jersey_no": 1},
			   {"name":"lovren", "jersey_no": 6},
			   {"name":"henderson", "jersey_no": 7},
			   {"name":"coutinho", "jersey_no": 10}]  

objlist = []	
	
class player(object):
	def __init__(self, player_name, jersey_no):
		self.player_name = player_name
		self.jersey_no = jersey_no
	
	def disp(self):
		print "name:", self.player_name, ",jersey no: ", self.jersey_no		
		

#player1 = player("mignolet", 1)
#player2 = player("coutinho", 10)
#player1.disp()
#player2.disp()
#***************************************************
objlist = []

for p in player_data:
	new = player(p['name'], p['jersey_no'])
	objlist.append(new)
print type(objlist)	
#***************************************************

print "*" * 100
for i in objlist:
	print i.disp()	