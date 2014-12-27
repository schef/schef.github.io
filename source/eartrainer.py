#!/usr/bin/python
# Public domain ear training program
# Written by Wojciech M. Zabolotny
# ( wzab@ise.pw.edu.pl )
# 1.07.2010
import random as r
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

NoteOnMode=False

class MidiReader:
  #This class reads the MIDI messages
  #and allows to wait for particular events
  def __init__(self,file_in):
    self.lastMsg=0
    self.fin = file_in
  def readByte(self):
    while True:
      b=self.fin.read(1)
      b=ord(b)
      if b<=127:
        return b
      else:
        self.lastMsg=b

  def waitNoteOn(self):
    while True:
      n=self.readByte()
      if self.lastMsg & 0xf0 == 0x90:
        #We are receiving NoteOn, and n is the note code
        v=ord(self.fin.read(1))
        if v>= 128:
           raise("Incomplete NoteOn message!")
        if v== 0:
           #This is NoteOff sent by some keyboards
           continue
        return n
               
  def waitNoteOff(self):
    #Some keyboards (e.g. E-MU Xboard 49) send
    #NoteOn with velocity=0 instaed of NoteOff
    while True:
      n=self.readByte()
      if self.lastMsg & 0xf0 == 0x90:
        #We are receiving NoteOn, and n is the note code
        v=ord(self.fin.read(1))
        if v>= 128:
           raise("Incomplete NoteOn message!")
        if v==0:
           #Yes, this is the NoteOn with velocity=0
           return
      elif self.lastMsg & 0xf0 == 0x80:
        #We are receiving NoteOff, and n is the note code
        v=ord(self.fin.read(1))
        if v>= 128:
           raise("Incomplete NoteOff message!")
        if v==0:
           #Yes, this is the NoteOff message
           return

midi=MidiReader(fin)  
while True:
  # Select random note
  note=r.randint(keymin,keymax)
  done = False
  while not done:
    fout.write(chr(0x90)+chr(note)+chr(127))
    fout.flush()
    time.sleep(0.5)
    fout.write(chr(0x80)+chr(note)+chr(127))
    fout.flush()
    print "Play the same note"
    n = midi.waitNoteOn()
    if n==note:
       print "Good!"
       done=True
    elif n<note:
       print "Too low!"
    elif n>note:
       print "Too high!"
    midi.waitNoteOff()
    time.sleep(0.5)
