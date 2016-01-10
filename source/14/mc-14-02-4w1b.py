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

print ("Exercise: 14-02")
print ("4 White tones, 1 tone. 30 Rounds.")

i = 0
noteCount = 0
whiteCorrect = 0
correct = 0

try:
 while True:
  print ("Possible commands: 1-again, 2-error, 3-correct, 4-compare-to-c, 5-next, <note name>:")
  noteCount += 1
  if noteCount % 5 == 0:
    note = random.choice(blackNotes)
    print("black")
  else:
    note = random.choice(whiteNotes)
  match = False
  noteError = None
  while not match: #here starts the practice
   done = False
   playNote(note)
   while not done:
    n = input("? ")
    if n =="1":
      playNote(note)
    elif n == "5":
      print ("Next")
      i += 1
      print (str(i) + ". round.")
      done = True
      match = True
    elif n =="2":
      if (noteError):
        print (num2Name(noteError) + " the error note.")
        playNote(noteError)
      else:
        print("You didn't guess.")
    elif n =="3":
      print (num2Name(note) + " the correct note.")
      playNote(note)
    elif n =="4":
      print ("C the comparrer")
      playNote(name2Num("c"))
    elif regSharp.match(n) or regFlat.match(n) or regWhite.match(n):
      if num2Name(note).lower() == n:
        done = True
        match = True
        print("Correct.")
        i += 1
        if noteCount %4 != 0:
            whiteCorrect += 1
        if noteCount %5 == 0 and whiteCorrect >= 3:
            correct +=1
        print (str(i) + ". round. " + str(correct) + " correct.")
      else:
        print ("Error.")
        noteError = name2Num(n)
        playNote(noteError)
        correct = 0
        whiteCorrect = 0
    elif re.compile("^t [a-z]+$").match(n):
      splitNote = n.split()
      playNote(name2Num(splitNote[1]))
except KeyboardInterrupt:
  pass
