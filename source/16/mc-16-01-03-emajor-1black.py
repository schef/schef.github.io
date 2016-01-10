#!/usr/bin/python3
#import time
import random
import imp
modl = imp.load_source('ppFunctions', '../00/ppFunctions.py')
import os
from ppFunctions import *
from termcolor import colored, cprint
#sleep becouse of loading midi modules
print("Are you ready?")
time.sleep(1)

print_status = lambda x: cprint(x, 'white', 'on_blue')
print_help = lambda x: cprint(x, 'red')

hit = 0
rounde = 1
done = False

generatedList = []
for i in range(stringToMidiNum("c"), stringToMidiNum("c'")+1):
  if i%12 in blackTonesBase:
    generatedList.append(i)
while True:
  try:
    os.system('clear')
    print_status("Status: round=" + str(rounde) + ", hit=" + str(hit))
    print_help("Help: rEPEAT sKIP")
    playHarmonicNotes(stringToMidiNum("e gis h"))
    randomNote = random.choice(generatedList)
    playNote(randomNote)
    while not done:
        guessedNote = input("Your input:")
        if guessedNote == "r":
            print("Repeating...")
            playHarmonicNotes(stringToMidiNum("e gis h"))
            playNote(randomNote)
        elif guessedNote == "s":
            print("Skiping...")
            done = True
        elif guessedNote not in lilypondTones:
            print("What? Syntax error!")
        else:
            if (lilypondTones[guessedNote] == randomNote%12):
                print("Yea!")
                hit += 1
                rounde += 1
                done = True
            else:
                print("Almost!")
                hit = 0
    done = False
  except (KeyboardInterrupt):
    print('...Program Stopped Manually!')
    raise
