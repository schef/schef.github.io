#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import sys
sys.path.append("/home/schef/github/schef.github.io/source/")
from pptraning import *

print ("Exercise 12-02:")
print ("Black melodic doubles OVR.")
#from c to c'' white tones

usage = "Usage: 1-repeat, <note> <note> \"c d\", ?-usage."
round = 1

try:
  print(usage)
  while True:
    noteOne = random.choice(blackNotes)
    while True:
      noteTwo = random.choice(blackNotes)
      if num2Name(noteOne) != num2Name(noteTwo):
        break
    match = False
    while not match:
      done = False
      playNote(noteOne)
      playNote(noteTwo)
      while not done:
        n = input("? ")
        if n == "1":
          playNote(noteOne)
          playNote(noteTwo)
        elif n == "?":
          print(usage)
        elif splitTwo.match(n):
          splitNote = n.split()
          if splitNote[0] == num2Name(noteOne).lower() and splitNote[1] == num2Name(noteTwo).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            playNote(name2Num(splitNote[0]))
            playNote(name2Num(splitNote[1]))
        elif regSharp.match(n) or regFlat.match(n):
          playNote(name2Num(n))
        elif n == "help":
          print(num2Name(noteOne), num2Name(noteTwo))
except KeyboardInterrupt:
  pass
