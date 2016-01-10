#!/usr/bin/python3
#import time
import random
import imp
modl = imp.load_source('ppFunctions', '../00/ppFunctions.py')
logo = imp.load_source('logo', '../00/logo.py')
from logo import *
import os
from ppFunctions import *
from termcolor import colored, cprint
os.system('clear')

#sleep becouse of loading midi modules
print_logo()
time.sleep(1)

print_status = lambda x: cprint(x, 'white', 'on_blue')
print_help = lambda x: cprint(x, 'red')

rounde = 1
done = False

generatedList = []
for i in range(stringToMidiNum("c"), stringToMidiNum("h")+1):
    if (i%12 in whiteTonesBase) or (i%12 == blackTones.get("as")):
        generatedList.append(i)
while True:
  try:
    os.system('clear')
    print_logo()
    print_status("Status: round=" + str(rounde))
    print_help("Help: pLAY nEXT")
    randomNote = random.choice(generatedList)
    generatedListTwo = list(generatedList)
    generatedListTwo.remove(randomNote)
    randomNoteTwo = random.choice(generatedListTwo)
    while not done:
        print(midiToString(randomNote) + " " + midiToString(randomNoteTwo))
        guessedNote = input("Your input: ")
        if guessedNote == "p":
            print("Playing...")
            playNote(randomNote)
            playNote(randomNoteTwo)
        elif guessedNote == "n":
            print("Next...")
            rounde += 1
            done = True
        else:
            print("What? Syntax error!")
    done = False
  except (KeyboardInterrupt):
    print('...Program Stopped Manually!')
    raise
