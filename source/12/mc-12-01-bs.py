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

print ("Exercise: 12-01")
print ("Black tones. OVR.")

i = 0

try:
 while True:
  print ("Possible commands: 1-again, 2-error, 3-correct, 4-compare-to-c, 5-next, <note name>:")
  note = random.choice(blackNotes)
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
    elif regSharp.match(n) or regFlat.match(n):
      if num2Name(note).lower() == n:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = name2Num(n)
        playNote(noteError)
except KeyboardInterrupt:
  pass
