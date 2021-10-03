# followed Brant's example from slide 15 of Session 3 pdf

#string

s = "I am a string"
print(type(s))	#retruns str

#Boolean
yes = True
print(type(yes))		#boolean True

no = False
print(type(no))			#Boolean False

# List -- ordered and changeable

alpha_list = ["a", "b", "c"] #list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#Tuple --order and unchangeable
alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))		#will say tuple

try: 							#attempt the following line
	alpha_tuple[2] = "d"		#won't work and will raise TypeError
except TypeError:				#when we get a TypeError
	print("We can't add elements to tuples") #print 
print(alpha_tuple)				#will print tuple		