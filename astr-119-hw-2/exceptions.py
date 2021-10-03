# followed Brant's example from slide 21 of Session 3 pdf

#python expections let you deal with 
#unexpected results

try:
	print(a)	#this will throw an exception since a is not defined 
except:	
	print("a is not defined!")

#There are specific errors to help with cases
try:
	print(a)	#this will throw an exception since a is not defined
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")		

#this will break our program
#since a is not defined
print(a)