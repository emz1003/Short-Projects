import turtle

def main():
	## User enters a word. @word is capitalized and put into a list
	word = raw_input('Enter a word: ')
	print type(word)
	word = list(word.upper())


	## organize word into list.  @wordNoDup holds all the different letters in the word.
	wordNoDup = list(set(word))
#	print wordNoDup

	print 100 * '\n'

	##
	# setup() : Major function that runs smaller functions of setting up
	#
	# Pre-condition: word has already been entered and modified
	# PostCondition: A noose, wordbank and dashes for the correct
	# 				 letters of @word will be drawn by turtles
	#/
	setup(word)

	##
	# gameGo() :
	gameGo(word)

#----------------------------------------------------------------------------------------#
#										    SETUP
#----------------------------------------------------------------------------------------#


def setup(word):
	print "drawing noose"
	drawNoose()

#	personI = 0

    # Draw the screen
	ticks = turtle.Turtle()
	ticks.penup()
	ticks.goto(-100,0)
	for i in range(len(word)):
		ticks.pendown()
		ticks.forward(20)
		ticks.penup()
		ticks.forward(20)

	wordBank = turtle.Turtle()
	wordBank.penup()
	wordBank.goto(-100,-100)

def drawNoose():
	noose = turtle.Turtle()
	noose.penup()
	noose.back(200)
	noose.pendown()
	noose.back(100)
	noose.forward(50)
	noose.left(90)
	noose.forward(200)
	noose.right(90)
	noose.forward(100)
	noose.right(90)
	noose.forward(25)

#----------------------------------------------------------------------------------------#
# 											GAMEGO
#----------------------------------------------------------------------------------------#

def gameGo(word):
	tries = 0
	## @gameStatus can be of three strings: "continue", "win", "lose"
	gameStatus = "continue"
	while gameStatus == "continue" and tries <= 6:
		## @guessWordBool checks to see if player wants to guess a word
		guessWordBool = raw_input("Do you want to guess the word? y/n: ")

		if guessWordBool == "y":
			gameStatus = guessWord(word,tries)[0]
#			print guessWord(word, tries)

		## Player guessed correctly .  exit out of loop
		if gameStatus == "win":
			break

		## If player didnt guess the word, ask player for a letter guess
		if gameStatus == "continue":
			print "Didnt code for guessing letters"
			guessLetter()

	# #
	# Deciding game status
	# #
	print "jumped out of loop; game status:", gameStatus
	if gameStatus == "win":
		print "YAY! You win!"


def guessWord(word,tries):
	reqWord = raw_input("What is your guess?")
	if list(reqWord.upper()) == word:
		## NOTE: find a more effecient way to retuern only @gameStatus. returning @tries is not necessary
		return "win", tries
	else:
		print "That's not correct!"
		eval(drawPerson[tries])()
		tries += 1
		return "continue", tries

def guessLetter(wordNoDup,tries):
	guessedLetter = raw_input("Guess a letter:")
	letterBool = false
	correctindex = []
	for i in wordNoDup:
		if guessedLetter.upper() == i:
			letterBool = true
			correctindex.append(i)


	if letterBool == false:
		tries += 1
		return "continue", tries
	else:
		return "continue", guessedLetter, correctindex


def drawHead():
        head = turtle.Turtle()
        head.penup()
        head.color('pink')
        head.goto(-150,125)
        head.pendown()
        head.circle(25)
def drawBody():
        body = turtle.Turtle()
        body.color('blue')
        body.penup()
        body.goto(-150, 125)
        body.right(90)
        body.pendown()
        body.forward(75)
def drawLegL():
        legL = turtle.Turtle()
        legL.color('blue')
        legL.penup()
        legL.goto(-150, 50)
        legL.right(120)
        legL.pendown()
        legL.forward(50)
def drawLegR():
        legR = turtle.Turtle()
        legR.color('blue')
        legR.penup()
        legR.goto(-150, 50)
        legR.right(60)
        legR.pendown()
        legR.forward(50)
def drawArmL():
        armL = turtle.Turtle()
        armL.penup()
        armL.goto(-150,100)
        armL.left(135)
        armL.pendown()
        armL.forward(50)
def drawArmR():
        armR = turtle.Turtle()
        armR.penup()
        armR.goto(-150,100)
        armR.left(45)
        armR.pendown()
        armR.forward(50)

drawPerson = ["drawHead", "drawBody", "drawLegL","drawLegR","drawArmL","drawArmR"]

main()
