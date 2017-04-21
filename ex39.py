print "Here is how a list works:\n\n"

things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things


print "\nHere is how a dictionary works:\n\n"

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print stuff['name']

print stuff['age']

print stuff ['height']

stuff ['city'] = "San Francisco"
print stuff['city']


print "\nHere is another example of how a dictionary works (objects other than strings):\n\n"

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]

print stuff[2]

print stuff


print "\nHere is another example of how a dictionary works (deleting):\n\n"

del stuff['city']
del stuff[1]
del stuff[2]

print stuff