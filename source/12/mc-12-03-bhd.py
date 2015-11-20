#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import sys

print ("Exercise 11-03:")
print ("Black harmonic doubles. OVR.")
sys.path.append("/home/schef/github/schef.github.io/source/")
from pptraning import *

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
    if noteTwo < noteOne:
      swap = noteOne
      noteOne = noteTwo
      noteTwo = swap
      swap = None
    match = False
    while not match:
      done = False
      playTwoNotes(noteOne, noteTwo)
      while not done:
        n = input("? ")
        if n == "1":
          playTwoNotes(noteOne, noteTwo)
        elif n == "?":
          print(usage)
        #TODO:bug da prima sve umjesto samo imena nota
        elif splitTwo.match(n):
          splitNote = n.split()
          if splitNote[0] == num2Name(noteOne).lower() and splitNote[1] == num2Name(noteTwo).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            playTwoNotes(name2Num(splitNote[0]), name2Num(splitNote[1]))
        elif b.match(n):
          playNote(name2Num(n))
        elif n == "help":
          print(num2Name(noteOne), num2Name(noteTwo))
except KeyboardInterrupt:
  pass
