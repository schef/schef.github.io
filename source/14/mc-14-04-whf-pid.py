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
print ("White harmonic fours. Pitch indentification drill. OVR.")

runda = 0

try:
 while True:
  runda += 1
  print ("Possible commands: 1-again, 2-play, 3-next, 4-compare-to-c:")
  while True:
    notes = []
    for i in range(0, 4):
      notes.append(random.choice(whiteNotes[7:28]))
#    if len(list(set(notes))) == 4:
#      break;
    if (len(list(set(notes))) == 4 \
        and (notes[0]%12 != notes[1]%12) \
        and (notes[0]%12 != notes[2]%12) \
        and (notes[0]%12 != notes[3]%12) \
        and (notes[1]%12 != notes[2]%12) \
        and (notes[1]%12 != notes[3]%12) \
        and (notes[2]%12 != notes[3]%12) \
       ):
      break;

  #notes.sort()
  match = False
  noteError = None
  while not match: #here starts the practice
   done = False
   #playFourNotes(notes)
   playNote(notes[0])
   playNote(notes[1])
   playNote(notes[2])
   playNote(notes[3])
   while not done:
    n = input("? ")
    if n =="1":
      #playFourNotes(notes)
      playNote(notes[0])
      playNote(notes[1])
      playNote(notes[2])
      playNote(notes[3])
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
      print(num2Name(notes[0]), num2Name(notes[1]), num2Name(notes[2]), num2Name(notes[3]))
    elif re.compile("^[0-3] [0-3]$").match(n):
      splited = n.split()
      playTwoNotes(notes[int(splited[0])], notes[int(splited[1])])
    elif re.compile("^[0-3] [0-3] [0-3]$").match(n):
      splited = n.split()
      playThreeNotes(notes[int(splited[0])], notes[int(splited[1])], notes[int(splited[2])])
    elif splitFour.match(n):
      splitNote = n.split()
      if splitNote[0] == num2Name(notes[0]).lower() and splitNote[1] == num2Name(notes[1]).lower() and splitNote[2] == num2Name(notes[2]).lower() and splitNote[3] == num2Name(notes[3]).lower():
        print ("Next")
        print (str(runda) + ". round.")
        done = True
        match = True
except KeyboardInterrupt:
  pass
