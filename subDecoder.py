# Decode .sub File
# https://www.youtube.com/watch?v=LEyna1X_2dY

import re, statistics, binascii, pprint
import tkinter as tk
from tkinter import filedialog

Harcoded = True

def open_file():
    if(Harcoded):
       return '''C:/Users/tybea/Downloads/Jj2.sub'''
    else:
        return filedialog.askopenfilename(filetypes=[("Subtitle files", "*.sub")])

# Define the regular expression pattern to find
pattern = r'(-\d+ )'  # This pattern matches a negative number followed by a space
replacement = r',\1\n'  # This replaces the matched pattern with a comma, $1 (captures the matched number), and a newline

# For the PiShock dont go below 0.01 ig?
SilenceTolerance = 0.1 # Measured in Milliseconds
SilenceTolerance_uS = 500
DEFAULTVALUE = '1'
# Tone < 100   Silence > 1000 = 0
# Tone > 1000  Silence < 500  = 1

# Note, theres a weird pattern going on with JJ2, Raw Sample ahead:
''' Cool Shit Ig, find me out later
Break Found at line 1, size of   1    Just the Start IG
Break Found at line 45, size of  44  1
Break Found at line 89, size of  44  2
Break Found at line 133, size of 44  3
Break Found at line 177, size of 44  4
Break Found at line 221, size of 44  5
Break Found at line 265, size of 43======
Break Found at line 309, size of 44  1
Break Found at line 353, size of 44  2
Break Found at line 397, size of 44  3
Break Found at line 441, size of 44  4
Break Found at line 485, size of 44  5
Break Found at line 529, size of 43======
Break Found at line 573, size of 44  1
Break Found at line 617, size of 44  2
Break Found at line 661, size of 44  3
Break Found at line 705, size of 44  4
Break Found at line 749, size of 44  5
Break Found at line 793, size of 43======
Break Found at line 837, size of 44  1
Break Found at line 881, size of 44  2
Break Found at line 925, size of 44  3
Break Found at line 969, size of 44  4
Break Found at line 1013, size of 44 5
'''

with open(open_file(), 'r', encoding='utf-8') as file:
    FileContents = file.read().split('\n')

    # Header Info
    FileType  = FileContents[0]
    Version   = FileContents[1]
    Frequency = FileContents[2]
    Preset    = FileContents[3]
    Protocol  = FileContents[4]

    ''' 
    What you get out of it
        - tone, silence (uSeconds, 1000uS = 1millisecond)

    Notes:
        - Probably should ignore the first lil bit of the file
        - Need to Figure out how long the silence is for tho to help make this up
    '''
    

    Tone_Silence_Data = []
    Tones = []
    Silence = []
    # Loop through the data and process it
    for j in range(5, len(FileContents)):
        Stripped_RAW_DATA = FileContents[j][10:]
        Stripped_RAW_DATA = re.sub(pattern, replacement, Stripped_RAW_DATA)
        Stripped_RAW_DATA = Stripped_RAW_DATA.replace(' ,-', ', -')
        
        # Split the data into packets and process each packet
        packets = Stripped_RAW_DATA.splitlines()
        
        for packet in packets:
            try:
                tone, silence = packet.split(', -')
                Tones.append(int(tone))
                Silence.append(int(silence))
                Tone_Silence_Data.append((tone, silence))
            except ValueError:
                print(f"Failed to Interpret a packet: {packet}")

    # Join the processed data with newline characters
    RawCombined = '\n'.join(FileContents[5:])
    print(Tone_Silence_Data)
    print(sorted(Tones))
    TonesMedian =   statistics.median(Tones)
    SilenceMedian = statistics.median(Silence)

    print(TonesMedian, SilenceMedian)

    # Tone < 100   Silence > 1000 = 0
    # Tone > 1000  Silence < 500  = 1
    
    # Scuffed Idea, but to calculate the tolerances, just get the mean of both all of the tones and frequences

    breakpackets = 0
    biggestVal   = 0
    totalLength  = 0
    PacketLenghtArray = []
    nibbleCounter = 0
    Nibbles = []
    nibble = ''
    for i in range(len(Tone_Silence_Data)):
        packet = Tone_Silence_Data[i]
        if(len(packet) == 2):
            
            tone    = int(packet[0])
            silence = int(packet[1])

            if(nibbleCounter >= 4):
                nibbleCounter = 0
                Nibbles.append(hex(int(nibble, 2)))
                nibble = ''
            
            if tone < TonesMedian and silence > SilenceMedian:
                nibble += '0'
            elif tone > TonesMedian and silence < SilenceMedian:
                nibble += '1'

            else:
                nibble += str(DEFAULTVALUE)
                #print('ERROR')
            nibbleCounter += 1


            biggestVal += 1
            totalLength += silence
            if(silence > SilenceTolerance):
                #print(f'Break Found at line {i}, size of {biggestVal}')
                PacketLenghtArray.append(biggestVal)
                breakpackets += 1
                biggestVal = 0
            #print(f'{silence}ms')
        else:
            #print("Invalid Packet")
            1 == 1

    print(f'\n\nBreak Packets: {breakpackets}\nSilence Tolerance: {SilenceTolerance}\nTotal Length: {round(totalLength, 4)}ms')
    print( statistics.median(PacketLenghtArray))
    for i in range(len(Nibbles)):
        print(Nibbles[i][2:], end='')
    
