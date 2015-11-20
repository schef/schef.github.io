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

print ("Exercise 11-05:")
print ("Black melodic triples. OVR")
#from c to c'' white tones

usage = "Usage: 1-repeat, <note> <note> \"c d e\", ?-usage."
round = 1

try:
  print(usage)
  while True:
    noteOne = random.choice(blackNotes)
    while True:
      while True:
        noteTwo = random.choice(blackNotes)
        if num2Name(noteOne) != num2Name(noteTwo):
          break
      while True:
        noteThree = random.choice(blackNotes)
        if num2Name(noteOne) != num2Name(noteTwo):
          break
      if num2Name(noteOne) != num2Name(noteThree):
        break
    match = False
    while not match:
      done = False
      playNote(noteOne)
      playNote(noteTwo)
      playNote(noteThree)
      while not done:
        n = input("? ")
        if n == "1":
          playNote(noteOne)
          playNote(noteTwo)
          playNote(noteThree)
        if n == "?":
          print(usage)
        if n == "help":
          print(num2Name(noteOne).lower(), num2Name(noteTwo).lower(), num2Name(noteThree).lower())
        elif splitThree.match(n):
          splitNote = n.split()
          if splitNote[0] == num2Name(noteOne).lower() and splitNote[1] == num2Name(noteTwo).lower() and splitNote[2] == num2Name(noteThree).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            playNote(name2Num(splitNote[0]))
            playNote(name2Num(splitNote[1]))
            playNote(name2Num(splitNote[2]))
except KeyboardInterrupt:
  pass
