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
print ("Major and minor seconds (harmonicly, only white tones). And were singing it from the bottom up (melodicly). A little bit of an ear teaser for you to sort out the top tone from the bottom tone. As you continue they clearify. When you can sing it then your ear has open up that much more.")
#from c to c'' white tones

notes = [ 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76 ]

i = 0

try:
 while True:
  note = random.choice(notes[:-2])
  noteTwo = notes[notes.index(note)+1]
  done = False
  print ("Possible commands: (a)gain, (n)ext, (l)ower, (u)pper:")
  fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(2.0)
  fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
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
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
      fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="l":
      fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="u":
      fout.write((chr(0x90)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(noteTwo)+chr(127)).encode('utf-8'))
      fout.flush()
except KeyboardInterrupt:
  pass
