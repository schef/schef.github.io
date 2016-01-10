#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import sys
import time
import re
sys.path.append("/home/schef/github/schef.github.io/source/")
from pptraning import *

print ("Exercise 14-01:")
print ("C major chord. We play the chord and then play any black tone and name it. OVR.")

usage = "Usage: 1-repeat, <note> \"d\", ?-usage."
round = 1

try:
  print(usage)
  while True:
    noteOne = random.choice(blackNotes)
    match = False
    while not match:
      done = False
      playThreeNotes(name2Num("c"), name2Num("e"), name2Num("g"))
      time.sleep(0.5)
      playNote(noteOne)
      while not done:
        n = input("? ")
        if n == "1":
          playThreeNotes(name2Num("c"), name2Num("e"), name2Num("g"))
          time.sleep(0.5)
          playNote(noteOne)
        elif n == "?":
          print(usage)
        elif regFlat.match(n) or regSharp.match(n):
          if n == num2Name(noteOne).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            playNote(name2Num(n))
            round = 1
        elif regSharp.match(n) or regFlat.match(n):
          playNote(name2Num(n))
        elif n == "help":
          print(num2Name(noteOne))
        elif re.compile("^t [a-z]+$").match(n):
          splitNote = n.split()
          playNote(name2Num(splitNote[1]))
except KeyboardInterrupt:
  pass
