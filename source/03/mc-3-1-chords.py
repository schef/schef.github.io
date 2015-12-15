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

toneOffset = -24
#c major scale
fis = 66+toneOffset
es = 63+toneOffset

opcije = [ fis, es ]
dur = [ 0, 4, 7, 12 ]
notes = [ 60+toneOffset, 62+toneOffset, 64+toneOffset, 65+toneOffset, 67+toneOffset, 69+toneOffset, 71+toneOffset ]
try:
 while True:
  note=random.choice(opcije)
  done = False
  print ("Possible commands: (a)gain, (n)ext:")
  while not done:
    if note == 66:
      print ("fis-dur")
    elif note == 63:
      print ("es-dur")
    fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
    fout.write((chr(0x90)+chr(note+dur[1])+chr(127)).encode('utf-8'))
    fout.write((chr(0x90)+chr(note+dur[2])+chr(127)).encode('utf-8'))
    fout.write((chr(0x90)+chr(note+dur[3])+chr(127)).encode('utf-8'))
    fout.flush()
    time.sleep(2)
    fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
    fout.write((chr(0x80)+chr(note+dur[1])+chr(127)).encode('utf-8'))
    fout.write((chr(0x80)+chr(note+dur[2])+chr(127)).encode('utf-8'))
    fout.write((chr(0x80)+chr(note+dur[3])+chr(127)).encode('utf-8'))
    fout.flush()
    n = input("? ")
    if n == "n":
      print ("Next")
      done = True
    elif n =="a":
      pass
except KeyboardInterrupt:
  pass
