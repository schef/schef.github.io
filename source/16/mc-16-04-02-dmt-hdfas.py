#!/usr/bin/python3
#import time
import random
import imp
modl = imp.load_source('ppFunctions', '../00/ppFunctions.py')
logo = imp.load_source('logo', '../00/logo.py')
import os
from ppFunctions import *
from termcolor import colored, cprint
os.system('clear')
from logo import *
#sleep becouse of loading midi modules
print_logo()
time.sleep(1)

print_status = lambda x: cprint(x, 'white', 'on_blue')
print_help = lambda x: cprint(x, 'red')

hit = 0
rounde = 1
done = False


choiceList = [ "h,", "d", "f", "as"]
generatedList = []
for i in choiceList:
    generatedList.append(stringToMidiNum(i))
while True:
  try:
    os.system('clear')
    print_logo()
    print_status("Status: round=" + str(rounde) + ", hit=" + str(hit))
    print_help("Help: rEPEAT sKIP")
    randomNote = random.choice(generatedList)
    generatedListTwo = list(generatedList)
    generatedListTwo.remove(randomNote)
    randomNoteTwo = random.choice(generatedListTwo)
    playNote(randomNote)
    playNote(randomNoteTwo)
    while not done:
        guessedNote = input("Your input: ")
        splitedGuessedNotes = guessedNote.split()
        if guessedNote == "r":
            print("Repeating...")
            playNote(randomNote)
            playNote(randomNoteTwo)
        elif guessedNote == "s":
            print("Skiping...")
            done = True
        elif any([x for x in splitedGuessedNotes if x not in lilypondTones]):
            print("What? Syntax error!")
        else:
            if (lilypondTones[splitedGuessedNotes[0]] == randomNote%12 and lilypondTones[splitedGuessedNotes[1]] == randomNoteTwo%12):
                print("Yea!")
                hit += 1
                rounde += 1
                done = True
            else:
                print("Almost!")
                playNote(randomNote)
                playNote(randomNoteTwo)
                playNote(lilypondTones[splitedGuessedNotes[0]]+60)
                playNote(lilypondTones[splitedGuessedNotes[1]]+60)
                hit = 0
    done = False
  except (KeyboardInterrupt):
    print('...Program Stopped Manually!')
    raise
