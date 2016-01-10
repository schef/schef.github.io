import time
import rtmidi
import re

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

#if available_ports:
#        midiout.open_port(0)
#else:
midiout.open_virtual_port("My virtual output")

#note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
#note_off = [0x80, 60, 0]
#midiout.send_message(note_on)
#time.sleep(0.5)
#midiout.send_message(note_off)
noteTimeDur = 1

def noteOn(midiNum):
    #return([0x90, midiNum, 112])
    midiout.send_message([0x90, midiNum, 112])
def noteOff(midiNum):
    #return([0x80, midiNum, 0])
    midiout.send_message([0x80, midiNum, 0])

def playNote(midiNum):
    noteOn(midiNum)
    time.sleep(noteTimeDur)
    noteOff(midiNum)

def playMelodicNotes(midiTup):
    for i in midiTup:
        playNote(i)

def playHarmonicNotes(midiTup):
    for i in midiTup:
        noteOn(i)
    time.sleep(noteTimeDur)
    for i in midiTup:
        noteOff(i)

noteOffset = 60

lilypondOctaves = {
    ",,," : -3,
    ",," : -2,
    "," : -1,
    "" : 0,
    "'" : 1,
    "''" : 2,
    "'''" : 3
}

lilypondTones = {
    "c" : 0,
    "cis" : 1,
    #"des" : 1,
    "d" : 2,
    #"dis" : 3,
    "es" : 3,
    "e" : 4,
    #"eis" : 5,
    #"fes" : 4,
    "f" : 5,
    "fis" : 6,
    #"ges" : 6,
    "g" : 7,
    #"gis" : 8,
    "as" : 8,
    "a" : 9,
    #"ais" : 10,
    "b" : 10,
    "h" : 11,
}

def stringToMidiNum(string):
    tonovi = re.split(" +", string)
    listaTonova = []
    for i in tonovi:
        base = re.sub(r"[',]+", "", i)
        octave = re.sub(r"\w+", "", i)
        midiNote = noteOffset + lilypondTones[base] + lilypondOctaves[octave]*12
        listaTonova.append(midiNote)
    if len(listaTonova) > 1:
        return(listaTonova)
    else:
        return(listaTonova[0])

def midiToString(midi):
    notes = []
    for k,v in lilypondTones.items():
        if v == midi%12:
            notes.append(k)
    if len(notes) > 1:
        return(notes[0] + "|" + notes[1])
    else:
        return(notes[0])

whiteTones = {
    "c" : 0,
    "d" : 2,
    "e" : 4,
    "f" : 5,
    "g" : 7,
    "a" : 9,
    "b" : 10,
    "h" : 11,
}

blackTones = {
    "cis" : 1,
    "des" : 1,
    "dis" : 3,
    "es" : 3,
    "fis" : 6,
    "ges" : 6,
    "gis" : 8,
    "as" : 8,
    "ais" : 10,
    "b" : 10,
}

whiteTonesBase = (0, 2, 4, 5, 7, 9, 11)
blackTonesBase = (1, 3, 6, 8, 10)

#generiramo listu tonova za vjezbu
lowTone = stringToMidiNum("c")
highTone = stringToMidiNum("c'")
