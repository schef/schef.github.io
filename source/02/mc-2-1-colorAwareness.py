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

notesOffset = -24
#c major scale
notes = [ 60+notesOffset, 62+notesOffset, 64+notesOffset, 65+notesOffset, 67+notesOffset, 69+notesOffset, 71+notesOffset ]
try:
 while True:
  note=random.choice(notes)
  done = False
  print ("Possible commands: (a)gain, (n)ext:")
  while not done:
    fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
    fout.flush()
    time.sleep(1.5)
    fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
    fout.flush()
    n = input("? ")
    if n == "n":
      print ("Next")
      done = True
    elif n =="a":
      pass
except KeyboardInterrupt:
  pass
