#!/usr/bin/python3

import argparse
import re
import json

toolbox={}

parser = argparse.ArgumentParser(description='Translate Excellon .xln files to gcode for CNC3018')
parser.add_argument('filename', help='xln (text) file')
parser.add_argument('-w', type=argparse.FileType('w', encoding='latin-1'), dest='outfile', help='the output file')
args = parser.parse_args()

File = open(args.filename,"r")
lines=File.read()

jobj = json.loads(lines)

outstring=";Generated with json2gcode.py (c) Jean PINON 2024\n\
G90\n\
G21\n\
M05\n"

zUpPosition=4.00000
zDownPosition=0.00000
zDepth=-3.1
zStep=0.5
plugeSpeed=203.0


outstring+="G0Z"+str(zUpPosition)+"\n"

toolbox=jobj['tools']

currenttool='-'

for h in jobj['holes']:
    if currenttool!=h['tool']:
        currenttool=h['tool']
        outstring=outstring+"M0 ;"+currenttool+"\n"
        outstring=outstring+"M03S10000\n"
    
    outstring=outstring+";drill\nG0X"+str(h['x'])+"Y"+str(h['y'])+"Z"+str(zUpPosition)+"\n"
    # go to firts position
    outstring=outstring+"G1Z"+str(zDownPosition)+"F"+str(plugeSpeed)+"\n"
    # Now drill\nG0
    z=zDownPosition
    while z>zDepth:
        z=z-zStep
        if (z<zDepth):
            z=zDepth
        outstring+="G1Z"+str(z)+"F"+str(plugeSpeed)+"\n"
        # go to top
        outstring=outstring+"G0Z"+str(zUpPosition)+"\n"

outstring+="G0X0Y0Z"+str(zUpPosition)

outstring+="G1\nM05\nM02\n"


if (args.outfile):
    args.outfile.write(outstring)
    args.outfile.close()
else:
    print (outstring)
