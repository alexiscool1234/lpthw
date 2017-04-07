from sys import argv

script, profile_file = argv


def main(profile_data):
	print "You are in a spooky room with four walls and three doors."
	choice = int(raw_input("Which door do you pick, 1, 2 or 3? "))
	
	if choice == 1:
		room1()
	elif choice == 2:
		room2()
	elif choice == 3:
		room3()
	else:
		print "Pick a number between 1-3 you mong."
		main()
		
		
def room1():
	print "meme."
	

def room2():
	print "meme."
	

def room3():
	print "meme."
	

def edit_char(profile_file):
	profile_data = open(profile_file)
	print "Here is your profile data:\n\n%s" % profile_data.read()
	
	profile_data.close()
	profile_data = open(profile_file, 'w')
	
	profile_list = []
	print "Please create your new profile:"
	
	profile_list.append("Sex: " + raw_input("Sex: ") + "\n")
	profile_list.append("Name: " + raw_input("Name: ") + "\n")
	profile_list.append("Height: " + raw_input("Height (feet'inches): ") + "\n")
	profile_list.append("Weight: " + raw_input("Weight (lbs): "))
	
	for i in profile_list:
		profile_data.write(i)
	
	profile_data.close()
	profile_data = open(profile_file)
	print "Here is your profile data:\n\n%s" % profile_data.read()
	profile_data.close()
	main(profile_data)
	
	
def current_char(profile_file):
	profile_data = open(profile_file)
	print "Here is your profile data:\n\n%s" % profile_data.read()
	main(profile_data)


def profile():
	print "You have provided the file %s as your profile." % profile_file
	answer = int(raw_input("Press 1 to Display\nPress 2 to Edit\nPress 3 to Continue: "))
	
	if answer == 1:
		current_char(profile_file)
		profile()
	elif answer == 2:
		edit_char(profile_file)
	elif answer == 3:
		current_char(profile_file)
		main()
	else:
		print "Invalid input"
		profile()


profile()