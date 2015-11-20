#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import sys

#c major scale
print ("Exercise 14-05:")
print ("As added.")
sys.path.append("/home/schef/github/schef.github.io/source/")
from pptraning import *


usage = "Usage: 1-play, 2-next."
round = 1

customBlackNotes = []
for i in range(len(blackNotes)):
  if i % 5 == 0:
    customBlackNotes.append(blackNotes[i+3])
print(customBlackNotes)

try:
  print(usage)
  while True:
    note = random.choice(whiteNotes + customBlackNotes)
    match = False
    while not match:
      print (num2Name(note))
      done = False
      while not done:
        n = input("? ")
        if n == "?":
          print(usage)
        elif n == "1":
          playNote(note)
        elif n == "2":
          round += 1
          print("Next round. " + str(round) + ".:")
          done = True
          match = True
        elif regWhite.match(n) or regFlat.match(n) or regSharp.match(n):
          playNote(name2Num(n))
except KeyboardInterrupt:
  pass
