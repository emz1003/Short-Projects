import turtle

def main():
        # someone enters in a word
        word = raw_input('Enter a word: ')
        
        wordNoDup = list(set(word.upper()))
        checkNoDup = []
        
        # variable check is a list form of the original word.  All capitalized
        check = list(word.upper())
        print 100 * '\n'

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
        
        switch = 0
        while personI < 6:
                if len(wordNoDup) == len(checkNoDup):
                        print 'You win!'
                        return
                guess = raw_input('Enter a letter: ')
                guess = guess.upper()
                print 'Your guess: ',guess
                ticks.penup()

 
                
                if guess == 'WORD':
                        wordGuess = raw_input('What is your guess?  ')
                        wordGuess = wordGuess.upper()
                        if wordGuess == word.upper():
                                print 'You win!'
                                ticks.goto(-100,-50)
                                for letters in word:
                                        ticks.forward(10)
                                        ticks.write(letters, False, align = 'center', font = ('Arial', 16, 'normal'))
                                        ticks.forward(30)
                                return 
                        else:
                                print 'Not yet...'
                                personI = drawing(personI,ticks,word)
                                personI += 1
 
                                
                                

                else:
                        personI = guessletter(ticks, check, guess,switch, personI,wordBank,word,checkNoDup)
                #print 'personI after: ', personI

def guessletter(ticks, check, guess,switch,personI,wordBank,word,checkNoDup):
        ticks.goto(-100,0)
        for letters in check:
                #print 'actual letter: ', letters
                #print 'Guess letter:',guess
                if guess == letters:
                        #print 'we have a match: ', letters
                        ticks.forward(10)
                        ticks.write(guess, False, align = 'center', font = ('Arial', 16, 'normal'))
                        ticks.forward(30)
                        switch = 1
                        #print 'switch: ',switch
                        #ticks.goto(-100,0)
                        # appends each guess to checkNoDup list
                        checkNoDup.append(guess)
                                
                else: 
                        #print 'We dont have a match', letters
                        ticks.forward(40)
        if switch == 0:
                personI = drawing(personI,ticks,word)
                wordBank.write(guess, False, align = 'center', font = ('Arial', 16, 'normal'))
                wordBank.forward(20)
        #print personI
        return personI
                                
                                
                

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
def drawing(personI,ticks,word):
        if personI == 0:
                        print 'drawing head'
                        drawHead()
                        personI += 1
                        print personI
        elif personI == 1:
                drawBody()
                print personI
                personI += 1
        elif personI == 2:
                drawLegL()
                personI += 1
        elif personI == 3:
                drawLegR()
                personI += 1
        elif personI == 4:
                drawArmL()
                personI += 1
        else: 
                drawArmR()
                personI += 1
                print 'You lose!'
                ticks.goto(-100,-50)
                for letters in word:
                        ticks.forward(10)
                        ticks.write(letters, False, align = 'center', font = ('Arial', 16, 'normal'))
                        ticks.forward(30)
        return personI

        
##drawNoose()
##drawHead()
##drawBody()
##drawLegL()
##drawLegR()
##drawArmL()
##drawArmR()
main()
