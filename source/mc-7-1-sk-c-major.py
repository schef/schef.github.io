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
print ("Exercise 7-1:")
print ("Reach out and play any white tone anywhere on the keyboard and name it. We're using the C major scale so you would know the tones by relative pitch. At this point we don't have full color discrimination. So the ear needs something to latch on to in order to know the tone. And thats fine if you know the tone by relative pitch. Just name the pitch. Don't be to hasty with your pitch naming. Go slowly. Listen to the tone. Take an interest in the tone. Allow a tone to soak for a moment. Something else is happening inside. If you get it wrong then pause. Listen to both tones. And you can even listen to it in a relationship to the C.")
#from c to c'' white tones

#c major scale
notes = [ 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96 ]
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
