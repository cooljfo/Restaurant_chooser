from random import randint

restoList = []

fo = open('restaurant.txt', 'r')

for line in fo:
	name, probability = line.split(': ')
	for x in range(0, int(probability)):
		restoList.append(name)
		
restaurant_number = randint(0,len(restoList))
print (restoList[restaurant_number])


fo.close()




