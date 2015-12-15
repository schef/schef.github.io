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
print ("Reach to your keyboard and play any two white tones that are separated by one white tone like e and g. Were just using the white tones only. Now we listen carefully to sound of these two tones. Listen individually so that you can hear each of the two tones. Usually we may only hear the top tone. So we have to listen little more closely to the bottom tone. Let your ear get inside to hear the bottom tone as well as the top tone. Now to prove that you really are hearing these tones we sing them (from the bottom up). When you can sing the tones then you have proved that you really have heard both tones. You didn't just hear the top one. If you can't hear the bottom tone than play it. Listen to it separately. Then play the two tones together again and see if you can now hear the bottom tone. Just work with your ear like this. Take your time. Work with this drill until you can any two tones separate by one white tone. You don't have to name the pitch. Were just singing the tones.")

#from c to c'' white tones
noteOffset = -12
#notes = [ 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76 ]
notes = [ 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76 ]

i = 0

try:
 while True:
  note = random.choice(notes[:-2])
  noteTwo = notes[notes.index(note)+2]
  done = False
  print ("Possible commands: (a)gain, (n)ext, (l)ower, (u)pper:")
  fout.write((chr(0x90)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(2.0)
  fout.write((chr(0x80)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
  fout.flush()
  while not done:
    n = input("? ")
    if n == "n":
      print ("Next")
      i += 1
      print (str(i) + ". round.")
      done = True
    elif n =="a":
      fout.write((chr(0x90)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
      fout.write((chr(0x90)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
      fout.write((chr(0x80)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="l":
      fout.write((chr(0x90)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(note+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
    elif n =="u":
      fout.write((chr(0x90)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
      time.sleep(2.0)
      fout.write((chr(0x80)+chr(noteTwo+noteOffset)+chr(127)).encode('utf-8'))
      fout.flush()
except KeyboardInterrupt:
  pass
