import re
import time
#sys.path.append("/home/schef/github/schef.github.io/source/")
#from pptraning import *


def num2Name(note):
  if note in noteC:
    return("c")
  elif note-1 in noteC:
    return("cis")
  elif note-2 in noteC:
    return("d")
  elif note-3 in noteC:
    return("es")
  elif note-4 in noteC:
    return("e")
  elif note-5 in noteC:
    return("f")
  elif note-6 in noteC:
    return("fis")
  elif note-7 in noteC:
    return("g")
  elif note-8 in noteC:
    return("as")
  elif note-9 in noteC:
    return("a")
  elif note-10 in noteC:
    return("b")
  elif note-11 in noteC:
    return("h")

def name2Num(name):
  if name == "c":
    return(60)
  elif name == "cis":
    return(61)
  elif name == "des":
    return(61)
  elif name == "d":
    return(62)
  elif name == "dis":
    return(62)
  elif name == "es":
    return(63)
  elif name == "e":
    return(64)
  elif name == "f":
    return(65)
  elif name == "fis":
    return(66)
  elif name == "ges":
    return(66)
  elif name == "g":
    return(67)
  elif name == "gis":
    return(67)
  elif name == "as":
    return(68)
  elif name == "a":
    return(69)
  elif name == "ais":
    return(70)
  elif name == "b":
    return(70)
  elif name == "h":
    return(71)

#fname="/dev/snd/midiC1D0"
fname="/dev/snd/midiC2D0"
#fname="/dev/snd/midiC3D0"
#fname="/dev/snd/midiC3D0"
fin=open(fname,"rb")
fout=open(fname,"wb")

noteC = [ 36, 48, 60, 72, 84, 96 ]

def playNote(note):
  fout.write((chr(0x90)+chr(note)+chr(100)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(note)+chr(100)).encode('utf-8'))
  fout.flush()

def playTwoNotes(noteOne, noteTwo):
  fout.write((chr(0x90)+chr(noteOne)+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(100)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(noteOne)+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(100)).encode('utf-8'))
  fout.flush()

def playThreeNotes(noteOne, noteTwo, noteThree):
  fout.write((chr(0x90)+chr(noteOne)+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteTwo)+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(noteThree)+chr(100)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(noteOne)+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteTwo)+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(noteThree)+chr(100)).encode('utf-8'))
  fout.flush()

def playFourNotes(notes):
  fout.write((chr(0x90)+chr(notes[0])+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(notes[1])+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(notes[2])+chr(100)).encode('utf-8'))
  fout.write((chr(0x90)+chr(notes[3])+chr(100)).encode('utf-8'))
  fout.flush()
  time.sleep(2)
  fout.write((chr(0x80)+chr(notes[0])+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(notes[1])+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(notes[2])+chr(100)).encode('utf-8'))
  fout.write((chr(0x80)+chr(notes[3])+chr(100)).encode('utf-8'))
  fout.flush()

whiteNotes = [ #36, 38, 40, 41, 43, 45, 47, #2.0 c-h
               47,
               48, 50, 52, 53, 55, 57, 59, #7-14
               60, 62, 64, 65, 67, 69, 71, #14-21
               72, 74, 76, 77, 79, 81, 83, #21-28
#               84, 86, 88, 89, 91, 93, 95, #28-35
#               96 ]                        #35-36
             ]

blackNotes = [ #37, 39, 42, 44, 46, #cis-b
               49, 51, 54, 56, 58,
               61, 63, 66, 68, 70,
               73, 75, 78, 80, 82,
#               85, 87, 90, 92, 94]
             ]

regWhite = re.compile("^[a-h]$")
regSharp = re.compile("^[a-h]is$")
regFlat = re.compile("^[a-h]es$|^[a-h]s$|b")

splitTwo = re.compile("^[a-hise]+ [a-hise]+$")
splitThree = re.compile("^[a-hise]+ [a-hise]+ [a-hise]+$")
splitFour = re.compile("^[a-hise]+ [a-hise]+ [a-hise]+ [a-hise]+$")
