## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a instance of class Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog's __init__ has a variable called Name
        self.name = name

## Cat is-a instance of class Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat's __init__ has a variable called Name
        self.name = name
		
	def meme(self, sausages):
		self.sausages = sausages
		if sausages == 1:
			print "Sausages!"
		else:
			print ":("


## Person is-a object Class
class Person(object):

    def __init__(self, name):
        ## Person's __init__ has a variable called Name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a instance of class Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee's __init__ has-a variable called Salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a instance of Fish
class Salmon(Fish):
    pass

## class Halibut is-a instance of Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet (called satan)
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()