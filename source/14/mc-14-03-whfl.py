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

print ("Exercise: 14-03")
print ("White harmonic fours. Unlock and sing. OVR.")

runda = 0
nameNotes = []

try:
 while True:
  runda += 1
  print ("Possible commands: 1-again, 2-play, 3-next, 4-compare-to-c:")
  while True:
    notes = []
    for i in range(0, 4):
      #notes.append(random.choice(whiteNotes[13:30]))
      notes.append(random.choice(whiteNotes[6:26])) #po mojoj klavijaturi
      #notes.append(random.choice(whiteNotes[0:7]))
      #notes.append(random.choice(whiteNotes[:29]))
    if len(list(set(notes))) == 4:
      break;
  notes.sort()
  match = False
  noteError = None
  while not match: #here starts the practice
   done = False
   playFourNotes(notes)
   while not done:
    n = input("? ")
    if n =="1":
      playFourNotes(notes)
    elif n == "3":
      print ("Next")
      print (str(runda) + ". round.")
      done = True
      match = True
    elif n =="5":
      print (num2Name(notes[0]), num2Name(notes[1]), num2Name(notes[2]), num2Name(notes[3]))
    elif n =="4":
      print ("C the comparrer")
      playNote(name2Num("c"))
    elif n =="2":
      playNote(notes[0])
      playNote(notes[1])
      playNote(notes[2])
      playNote(notes[3])
    elif re.compile("^[0-3] [0-3]$").match(n):
      splited = n.split()
      playTwoNotes(notes[int(splited[0])], notes[int(splited[1])])
    elif re.compile("^[0-3] [0-3] [0-3]$").match(n):
      splited = n.split()
      playThreeNotes(notes[int(splited[0])], notes[int(splited[1])], notes[int(splited[2])])
    elif re.compile("^t [a-z]+$").match(n):
      splitNote = n.split()
      playNote(name2Num(splitNote[1]))
except KeyboardInterrupt:
  pass
