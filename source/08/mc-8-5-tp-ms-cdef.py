#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import time
import sys

fname="/dev/snd/midiC2D0"
#fname=sys.argv[1]
fin=open(fname,"rb")
fout=open(fname,"wb")
#keymin=int(sys.argv[2])
#keymax=int(sys.argv[3])
#keymin=int(60)
#keymax=int(72)

#c major scale
print ("Exercise 8-5:")
print ("Team players. C, D, E and F. Melodic single. OVR.")
#from c to c'' white tones

#c major scale
notes = [ 36, 38, 40, 41, 48, 50, 52, 53, 60, 62, 64, 65, 72, 74, 76, 77, 84, 86, 88, 89, 96 ]
noteC = [ 36, 48, 60, 72, 84, 96 ]

i = 0

def playNote(note):
  fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
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

try:
 while True:
  print ("Possible commands: 1-again, 2-error, 3-correct, 4-compare-to-c, 5-next, <note name>:")
  note = random.choice(notes)
  match = False
  noteError = None
  while not match:
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
        print (nameNote(noteError) + " the error note.")
        playNote(noteError)
      else:
        print("You didn't guess.")
    elif n =="3":
      print (nameNote(note) + " the correct note.")
      playNote(note)
    elif n =="4":
      print ("C the comparrer")
      playNote(60)
    elif n =="c":
      if note in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 60
        playNote(noteError)
    elif n =="d":
      if note-2 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 62
        playNote(noteError)
    elif n =="e":
      if note-4 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 64
        playNote(noteError)
    elif n =="f":
      if note-5 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 65
        playNote(noteError)
    elif n =="g":
      if note-7 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 67
        playNote(noteError)
    elif n =="a":
      if note-9 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 69
        playNote(noteError)
    elif n =="h":
      if note-11 in noteC:
        done = True
        match = True
        print("Correct.")
        i += 1
        print (str(i) + ". round.")
      else:
        print ("Error.")
        noteError = 71
        playNote(noteError)
except KeyboardInterrupt:
  pass
