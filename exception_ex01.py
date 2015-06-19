# coding=utf-8

while True:
	
	try:
		x = int(raw_input("please enter a number: "))
		break
	except Exception as ex:
		print "Oops! That was no valid number. Try again..."
		print "Error message :", ex