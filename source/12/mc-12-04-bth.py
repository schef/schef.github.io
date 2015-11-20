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

print ("Exercise 12-04:")
print ("Black melodic triples.")

usage = "Usage: 1-repeat, <note> <note> \"c d e\", ?-usage."
round = 1

try:
  print(usage)
  while True:
    while True:
      noteOne = random.choice(blackNotes[:-2])
      if noteOne < 60:
        break
    print("one: " + str(noteOne))
    while True:
      while True:
        noteTwo = random.choice(blackNotes[:-1])
        print("two: " + str(noteTwo))
        if 80 > noteTwo > noteOne and num2Name(noteOne) != num2Name(noteTwo):
          break
      while True:
        noteThree = random.choice(blackNotes)
        print("three: " + str(noteThree))
        if noteThree > noteTwo and num2Name(noteOne) != num2Name(noteThree):
          break
      if num2Name(noteTwo) != num2Name(noteThree):
        break
    match = False
    while not match:
      done = False
      playThreeNotes(noteOne, noteTwo, noteThree)
      while not done:
        n = input("? ")
        if n == "1":
          playThreeNotes(noteOne, noteTwo, noteThree)
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
            playThreeNotes(name2Num(splitNote[0]), name2Num(splitNote[1]), name2Num(splitNote[2]))
except KeyboardInterrupt:
  pass
