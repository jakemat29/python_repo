player_data = [{"name":"mingolet", "jersey_no": 1},
			   {"name":"lovren", "jersey_no": 6},
			   {"name":"henderson", "jersey_no": 7},
			   {"name":"coutinho", "jersey_no": 10}]  


class player(object):
	def __init__(self, player_name, jersey_no):
		self.player_name = player_name
		self.jersey_no = jersey_no
	
	def set_player(self):
			return self.player_name
			return self.jersey_no
			
for p in range(0, len(player_data)):
	p.append(player(p['name'],p['jersey_no']))
	
for i in p:
		print i
				