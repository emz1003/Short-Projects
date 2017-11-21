import random
import csv

def main():
	name = raw_input('Enter your name: ')
	if name[-1] == 's':
		name = name + "'"	
	else:
		name = name + "'s"

	live = ['mansion','apartment','shack','house']
	nameOfBoy = []
	salary = []
	placeOfHoneymoon = []
	numberOfKids = []	
	car = []
	pet = []
	job = []

	addRandom = raw_input('Do you want a random item added to your categories?  Choose Y or N: ')
	if addRandom == 'Y':
		randomGen(nameOfBoy,salary,placeOfHoneymoon,numberOfKids,car,pet,job)
		print "Warning: You may find a piece of your future that wasn't what you expected."

	strings = ['nameOfBoy', 'salary', 'placeOfHoneymoon', 'numberOfKids', 'car', 'pet','job']
	L = [nameOfBoy, salary, placeOfHoneymoon, numberOfKids, car, pet,job]
	num = random.randint(7,17)

	userAns(L,strings)

	L = [live, nameOfBoy, salary, placeOfHoneymoon, numberOfKids, car, pet,job]
	ans = [live, nameOfBoy, salary, placeOfHoneymoon, numberOfKids, car, pet,job]

	crossOut(L,num)

	print name, 'Future: '
	print 'You will live in a', live[0],', married to', nameOfBoy[0] + '.  Your honeymoon was so fun and exciting!'
	print 'You and', nameOfBoy[0], 'went to', placeOfHoneymoon[0], '.  You will be a', job[0], ', earning', salary[0], 'dollars, and have a', car[0] + '.' 
	print 'You will have', numberOfKids[0],'kids and a',pet[0] + '.' + '\n' + '\n'
	
	# future = [name,live[0],nameOfBoy[0],salary[0],placeOfHoneymoon[0],numberOfKids[0],car[0],pet[0],job[0] + '\n']
	
	# with open('futures0001.csv','a') as saved:
	# 	writer = csv.writer(saved)
	# 	writer.write(future)
	# 	saved.close()

	# variable saved is the list we are writing into our csv
	saved =[name]

	for stuff in ans:
		item = stuff[0]
		saved.append(item)
		

	with open('userAnswers.csv','a') as f:
		writer = csv.writer(f)
		writer.writerow(saved)
	f.close()

def crossOut(L,num,):
	while L != []:
		for cate in L:
			#print 'CAtegory: ', cate
			#print 'num: ', num
			# conditional checks to see if you are in list MASH.
			if num <= len(cate):
				# crosses out the item based on your num counter
				#print cate,'crossing out'
				length = len(cate)
				#print 'Removing: ', cate[num - 1]
				cate.remove(cate[num - 1])
				# see how many items are left in the list: len(cate) - num
				# num is going to take in consideration to the items after the crossed out item
				num = 7 - (length - num)
				#print 'Cross out: new num before moving to next section', num
				if len(cate) == 1:
					L.remove(cate)
				# in list MASH, but cross out is not under MASH
			else:
				#print 'happy'
				#print 'skipped over', cate
				num -= len(cate)

def userAns(L,strings):
	otherAns = raw_input('Are your friends answering the categories for you?  Choose Y or N: ')
	if otherAns == 'Y':
		numPpl = raw_input('Enter the number of people playing: ')
	else: 
		numPpl = 3

	for items in strings:
		indexStrings = strings.index(items)
		for i in range(int(numPpl)):
			entry = raw_input('Enter a ' + items +': ')
			L[indexStrings].append(entry)

def randomGen(nameOfBoy,salary,placeOfHoneymoon,numberOfKids,car,pet,job):
	nameOfBoy.append(random.choice(['Tom Cruise', 'Tom Hanks', 'Zac Efron' , 'Harry Potter', 'Morgan Freeman', 'George Washington']))
	salary.append(random.randint(1,10))
	placeOfHoneymoon.append(random.choice(['Venice','Paris','Bali', "your parent's basement", "McDonald's",'the cemetary']))
	numberOfKids.append(random.randint(5,100))
	car.append(random.choice(['bicycle', 'motorcycle','unicycle','Lamborgini','Batmobile','BMW']))
	pet.append(random.choice(['fern','rock','cockroach','horse','white tiger','lion']))
	job.append(random.choice(['janitor','waitress','factory worker','astronomer','plastic surgeon','businesswoman']))



main()
