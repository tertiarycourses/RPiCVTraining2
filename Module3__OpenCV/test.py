a = int(input('enter a number : '))
print("The number you enter is ",a)

# import sqlite3

# db = sqlite3.connect('test.db')

# db.execute('update student set rank=? where name=?',(1,'Jane'))
# db.execute('update student set rank=? where name=?',(2,'Ally'))

# db.execute('delete from student where rank=5')
# list = db.execute('select * from student order by rank')

# for i in list:
# 	print(i)

# db.execute('insert into student (name,rank) values (?,?)',('Ally',1))
# db.execute('insert into student (name,rank) values (?,?)',('Jane',2))
# db.execute('insert into student (name,rank) values (?,?)',('Belinda',3))
# db.execute('insert into student (name,rank) values (?,?)',('Alfred',4))
# db.execute('insert into student (name,rank) values (?,?)',('Steve',5))
# db.commit()


# db.execute('create table subjects (subject text,students int, classes int)')
# db.commit()

# db.execute('insert into subjects (subject,students,classes) values (?,?,?)',('English',200,10))
# db.execute('insert into subjects (subject,students,classes) values (?,?,?)',('Chinese',50,8))
# db.execute('insert into subjects (subject,students,classes) values (?,?,?)',('Math',80,12))
# db.execute('insert into subjects (subject,students,classes) values (?,?,?)',('Science',80,12))
# db.commit()

# db.execute('delete from subjects where subject="Science"')
# list = db.execute('select * from subjects order by subject')

# for i in list:
# 	print(i)


# class Employee:
# 	empCount = 0
# 	def __init__(self,name,salary):
# 		self.name = name
# 		self.salary = salary
# 		Employee.empCount = Employee.empCount  + 1

# 	def __del__(self):
# 		Employee.empCount = Employee.empCount - 1

# 	def dispCount(self):
# 		print("No of Employee =  {}".format(Employee.empCount))

# 	def empInfo(self):
# 		print("{} salary is {}".format(self.name,self.salary))

# class FullTimeStaff(Employee):

# 	def __init__(self,name,salary,leave):
# 		super().__init__(name,salary)
# 		self.leave = leave

# 	def empInfo(self):
# 		print("{} salary is {} and leave is {}".format(self.name,self.salary,self.leave))


# class PartTimeStaff(Employee):

# 	def __init__(self,name,hrrate):
# 		super().__init__(name,0)
# 		self.hrrate = hrrate
# 		Employee.empCount = Employee.empCount - 1


# 	def __del__(self):
# 		pass

# 	def empInfo(self):
# 		print("{} hourly rate is {} per hour".format(self.name,self.hrrate))

#Tesitng
# e1 = FullTimeStaff('Ally',5000,21)
# e2 = FullTimeStaff('Jane',2000,18)
# e3 = PartTimeStaff('Belina',10)
# e1.dispCount()
# del e2
# e1.dispCount()

#Tesitng
# e1 = Employee('Ally',5000)
# e2 = Employee('Jane',2000)
# e3 = Employee('Belina',3000)
# e1.dispCount()
# del e2
# e1.dispCount()


# class Rect:

# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width

# 	def area(self):
# 		return self.length*self.width

# class Square(Rect):

# 	def __init__(self,length):
# 		super().__init__(length,length)

# 	def __del__(self):
# 		print("I am destroyed")

# 	def perimeter(self):
# 		return 4*self.length

# Testing
# s1 = Square(10)
# print(s1.area())
# print(s1.perimeter())


# Testing
# r1 = Rect(10,20)
# print(r1.area())

# class Counter:

# 	count = 0
# 	def increment(self):
# 		self.count = self.count + 1
		
# 	def incrementByN(self,n):
# 		self.count = self.count + n
		
# 	def reset(self):
# 		self.count = 0

# Testing
# c1 = Counter()
# c2 = Counter()
# c1.increment()
# print(c1.count)
# print(c2.count)
# c1.incrementByN(10)
# c2.incrementByN(5)
# print(c1.count)
# print(c2.count)

# c1.reset()
# print(c1.count)

class Animal:

	def __init__(self,legs,color):
		self.legs = legs
		self.color = color

	def talk(self):
		print("talk like an animal")

# class Cat(Animal):

# 	def __init__(self,legs,color,name):
# 		super().__init__(legs,color)
# 		self.name = name
	
# 	def talk(self):
# 		print("{} meow meow meow".format(self.name))

# class Dog(Animal):

# 	def __init__(self,legs,color,name):
# 		super().__init__(legs,color)
# 		self.name = name
	
# 	def talk(self):
# 		print("{} woof woof woof".format(self.name))


# def makeNoise(a):
# 	a.talk()

# c1 = Cat(4,'gray','ally')
# d1 = Dog(4,'white','puppy')

# makeNoise(d1)

# c1 = Cat(4,'gray','ally')
# c2 = Cat(4,'black','belinda')
# print(c1.legs)
# print(c1.color)
# print(c1.name)
# c1.talk()
# c2.talk()

# a1 = Animal(8,'black')
# print(a1.legs)
# print(a1.color)
# def fibo(n):
# 	a,b = 0,1
# 	for i in range(n):
# 		a,b = b,a+b
# 		yield a

# f = fibo(30)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))


# def fibo(n):
# 	a,b = 0,1
# 	f = []
# 	for i in range(n):
# 		a,b = b,a+b
# 		f.append(a)
# 	return f 


# def even(n):
# 	for i in range(n+1):
# 		if i%2 == 0:
# 			yield i 
# a = even(10000000000000000000000)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# def even(n):
# 	a = []
# 	for i in range(n+1):
# 		if i%2 == 0:
# 			a.append(i)
# 	return a

# b = even(1000000000000000)
# print(b)
# namelist = ['ally','jane','belinda']

# a = (name.upper() for name in namelist)
# print(next(a))
# print(next(a))
# print(next(a))

#a = [i for i in range(1000000000000000)]
# a = (i+1000 for i in range(10))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# a = 'Today is a great day'
# b = a.split()
# print(b)
# # c = [i[-1] for i in b]
# c = {i[-1] for i in b}
# print(c)

# a = []
# for i in range(10):
# 	a.append(i*i)
# a = [i*i for i in range(30) if not i%3==0 and not i%5==0 ]
# print(a)


