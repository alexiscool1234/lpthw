class Song(object):					# defines the Class
	
	def __init__(self, lyrics):		#  makes lyrics unique to this Class and creates the instance of the Class
		self.lyrics = lyrics		#  converts data passed to Class as "lyrics" variable
	
	def sing_me_a_song(self):		# defines a Function
		for line in self.lyrics:    # loop through lyrics lines
			print line				# print each line
	
	
	
	
	
		
happy_bday = Song(["Happy birthday to you",				#  pass happy birthday lyrics to Class Song
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",	#  pass bulls on parade lyrics to Class Song
						"With pockets full of shells"])



						
happy_bday.sing_me_a_song()								#  call the happy birthday lyrics and pass them to sing_me_a_song Function

bulls_on_parade.sing_me_a_song()						#  call the bulls_on_parade lyrics and pass them to sing_me_a_song Function

