import turtle

def main():
	## User enters a word. @word is capitalized and put into a list 
	word = raw_input('Enter a word: ')
	word = list(word.upper())


	## organize word into list.  @wordNoDup holds all the different letters in the word. 
	wordNoDup = list(set(word.upper()))
#	print wordNoDup
        
	print 100 * '\n'
	
	##
	# setup() : Major function that runs smaller functions of setting up
	#
	# Pre-condition: word has already been entered and modified
	# PostCondition: A noose, wordbank and dashes for the correct 
	# 				 letters of @word will be drawn by turtles
	##/
	setup(word)

	##
	# gameGo() : 
	gameGo()


def setup(word):
	drawNoose()

	personI = 0

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
	
def gameGo():
	compareGuess()

def compareGuess():
	
main()
