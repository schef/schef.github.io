#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import time
import sys
import re

fname="/dev/snd/midiC2D0"
#fname=sys.argv[1]
fin=open(fname,"rb")
fout=open(fname,"wb")
#keymin=int(sys.argv[2])
#keymax=int(sys.argv[3])
#keymin=int(60)
#keymax=int(72)

#c major scale
print ("Exercise 10-17:")
print ("Aural chord analisys. First you have to unlock the sound by ear. And then you have to indentify. It's a very powerful tehnique to stabilize perfect pitch.")
#from c to c'' white tones

#c major scale
notes = [ 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96 ]
noteC = [ 36, 48, 60, 72, 84, 96 ]

def playNote(noteOne, noteTwo, noteThree):
  fout.write((chr(0x90)+chr(noteOne)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteThree)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(noteOne)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteThree)+chr(127)).encode('utf-8'))
  fout.flush()

def nameNote(note):
  if note in noteC:
    return("C")
  elif note-2 in noteC:
    return("D")
  elif note-4 in noteC:
    return("E")
  elif note-5 in noteC:
    return("F")
  elif note-7 in noteC:
    return("G")
  elif note-9 in noteC:
    return("A")
  elif note-11 in noteC:
    return("H")

def name2Note(name):
  if name == "c":
    return(60)
  if name == "d":
    return(62)
  if name == "e":
    return(64)
  if name == "f":
    return(65)
  if name == "g":
    return(67)
  if name == "a":
    return(69)
  if name == "h":
    return(71)

usage = "Usage: 1-repeat, <note> <note> \"c d e\", ?-usage."
round = 1
a = re.compile("^[a-h] [a-h] [a-h]$")

try:
  print(usage)
  while True:
    while True:
      noteOne = random.choice(notes[:-2])
      if noteOne < 60:
        break
    print("one: " + str(noteOne))
    while True:
      while True:
        noteTwo = random.choice(notes[:-1])
        print("two: " + str(noteTwo))
        if 80 > noteTwo > noteOne and nameNote(noteOne) != nameNote(noteTwo):
          break
      while True:
        noteThree = random.choice(notes)
        print("three: " + str(noteThree))
        if noteThree > noteTwo and nameNote(noteOne) != nameNote(noteThree):
          break
      if nameNote(noteTwo) != nameNote(noteThree):
        break
    match = False
    while not match:
      done = False
      playNote(noteOne, noteTwo, noteThree)
      while not done:
        n = input("? ")
        if n == "1":
          playNote(noteOne, noteTwo, noteThree)
        if n == "?":
          print(usage)
        if n == "help":
          print(nameNote(noteOne).lower(), nameNote(noteTwo).lower(), nameNote(noteThree).lower())
        elif a.match(n):
          splitNote = n.split()
          if splitNote[0] == nameNote(noteOne).lower() and splitNote[1] == nameNote(noteTwo).lower() and splitNote[2] == nameNote(noteThree).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            playNote(name2Note(splitNote[0]), name2Note(splitNote[1]), name2Note(splitNote[2]))
except KeyboardInterrupt:
  pass
