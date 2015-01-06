#!/usr/bin/python
# Public domain ear training program
# Written by Wojciech M. Zabolotny
# ( wzab@ise.pw.edu.pl )
# 1.07.2010
import random
import time
import sys
fname="/dev/snd/midiC2D0"
#fname=sys.argv[1]
#keymin=int(sys.argv[2])
#keymax=int(sys.argv[3])
keymin=int(60)
keymax=int(72)
fin=open(fname,"rb")
fout=open(fname,"wb")

#c major scale
print ("Exercise:")
print ("Do three tones close. Reach out play any three tones one handed. We listen , we unlock the sounds with our ears so we here each note discretly and then we sing them from the bottom up. And we check ourselfs.")
#from c to c'' white tones

notes = [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84 ]

i = 0

try:
 while True:
  intervalOne = random.randint(1, 10)
  intervalTwo = random.randint(1, 11-intervalOne)
  match = False
  while not match:
    note = random.choice(notes)
    if note+intervalOne+intervalTwo in notes:
      noteTwo = notes[notes.index(note)+intervalOne]
      noteThree = notes[notes.index(note)+intervalOne+intervalTwo]
      match = True
  done = False
  print ("Possible commands: (a)gain, (n)ext, (l)ower, (u)pper:")
  fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteThree)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteThree)+chr(127)).encode('utf-8'))
  fout.flush()
  while not done:
    n = input("? ")
    if n == "n":
      print ("Next")
      i += 1
      print (str(i) + ". round.")
      done = True
    elif n =="a":
      fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
      fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.write((chr(0x90)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
      fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.write((chr(0x80)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="l":
      fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="m":
      fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="u":
      fout.write((chr(0x90)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="r":
      fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
      #time.sleep(0.7)
      fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
      #time.sleep(0.7)
      fout.write((chr(0x90)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(0.7)
      fout.write((chr(0x80)+chr(noteThree)+chr(127)).encode('utf-8'))
      fout.flush()
      #time.sleep(0.7)
except KeyboardInterrupt:
  pass
