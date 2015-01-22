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
print ("Exercise 10-3:")
print ("Harmonic seconds pitch indetification drill. Were not singing the tone. We only identify them.")
#from c to c'' white tones

#c major scale
notes = [ 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96 ]
#notes = [ 36, 38, 40, 48, 50, 52, 60, 62, 64, 72, 74, 76, 84, 86, 88, 96 ]
noteC = [ 36, 48, 60, 72, 84, 96 ]

def playNote(note):
  fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
  fout.flush()

def play2Notes(noteOne, noteTwo):
  fout.write((chr(0x90)+chr(noteOne)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(noteOne)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
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
  elif name == "d":
    return(62)
  elif name == "e":
    return(64)
  elif name == "f":
    return(65)
  elif name == "g":
    return(67)
  elif name == "a":
    return(69)
  elif name == "h":
    return(71)

usage = "Usage: 1-repeat, <note> <note> \"c d\", ?-usage., hint, err"
round = 1
a = re.compile("^[a-h] [a-h]$")
singleNote = re.compile("^[a-h]$")

try:
  print(usage)
  while True:
    noteOne = random.choice(notes[:-1])
    noteTwo = notes[notes.index(noteOne)+1]
    #while True:
    match = False
    while not match:
      done = False
      play2Notes(noteOne, noteTwo)
      while not done:
        n = input("? ")
        if n == "1":
          play2Notes(noteOne, noteTwo)
        elif n == "?":
          print(usage)
        elif n == "hint":
          print(nameNote(noteOne) + " " + nameNote(noteTwo))
        elif n == "err":
          play2Notes(name2Note(errorNoteOne), name2Note(errorNoteTwo))
        elif a.match(n):
          splitNote = n.split()
          if splitNote[0] == nameNote(noteOne).lower() and splitNote[1] == nameNote(noteTwo).lower():
            round += 1
            print("Correct. Next round. " + str(round) + ".:")
            done = True
            match = True
          else:
            play2Notes(name2Note(splitNote[0]), name2Note(splitNote[1]))
            errorNoteOne = splitNote[0]
            errorNoteTwo = splitNote[1]
        elif singleNote.match(n):
          playNote(name2Note(n)) 
except KeyboardInterrupt:
  pass
