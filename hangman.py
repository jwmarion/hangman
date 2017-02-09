#hangman.py
import sys
import os


fails = 0
word = "The quick brown fox jumps over the lazy dog"
cGuesses = []
fGuesses = []
win = False

def drawGallow(fails):
    if fails == 0:
        print "     +------+\n     |      |\n     |\n     |\n     |\n     |\n    ___"
    if fails == 1:
        print "     +------+\n     |      |\n     |      0\n     |\n     |\n     |\n    ___"
    if fails == 2:
        print "     +------+\n     |      |\n     |      0\n     |      |\n     |\n     |\n    ___"
    if fails == 3:
        print "     +------+\n     |      |\n     |      0\n     |     \|\n     |\n     |\n    ___"
    if fails == 4:
        print "     +------+\n     |      |\n     |      0\n     |     \|/\n     |\n     |\n    ___"
    if fails == 5:
        print "     +------+\n     |      |\n     |      0\n     |     \|/\n     |      |\n     |\n    ___"
    if fails == 6:
        print "     +------+\n     |      |\n     |      0\n     |     \|/\n     |      |\n     |     /\n    ___"
    if fails == 7:
        print "     +------+\n     |      |\n     |      0\n     |     \|/\n     |      |\n     |     / \ \n    ___"

def checkGuess(guess):
    global fails
    check = False
    present = False
    for x in xrange(len(word)):
        if word[x].upper() == guess.upper():
            present = True
    if present == False:
        fails += 1
        fGuesses.append(guess)
    else:
        for x in xrange(len(cGuesses)):
            if guess == cGuesses[x]:
                check = True
        if check == False:
            cGuesses.append(guess)


def getLine():
    global win
    wincheck = True
    for x in xrange(len(word)):
        present = False
        for y in xrange(len(cGuesses)):
            if word[x].upper() == cGuesses[y].upper():
                sys.stdout.write(cGuesses[y])
                present = True
        if present == False:
            sys.stdout.write("_ ")
            wincheck = False
    if wincheck == True:
        win = True;
    print ""




while True:
    os.system('clear')
    drawGallow(fails)
    getLine()

    if fails >=7:
        print "LOSER! D:"
        break
    if win == True:
        print "You win! Congrats! :D"
        break

    pick = raw_input("Pick a letter! ")
    checkGuess(pick)
