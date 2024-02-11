#!/usr/bin/python3

import argparse
import re

tool=[]
currentTool='-'
hole=[]

parser = argparse.ArgumentParser(description='Translate Excellon .xln files to standard JSON description')
parser.add_argument('filename', help='xln (text) file')
parser.add_argument('-w', type=argparse.FileType('w', encoding='latin-1'), dest='outfile', help='the output file')
args = parser.parse_args()

File = open(args.filename,"r")
lines=File.readlines()

for ln in lines:
    ln=ln.rstrip() 
    # If tool       T1C2.108
    if (re.search(r'^T.+C.',ln)):
        tid=re.sub(r'C.*',"",ln)
        tsize=float(re.sub(r'T.+C',"",ln))
        tool.append({'id':tid,'size':tsize})
    # if TOOL SELECT
    if (re.search(r'^T[0-9]+$',ln)):
        currentTool=ln
    #if hole drilling X21590Y2540
    if (re.search(r'^X[0-9]+Y[0-9]+$',ln)):
        x=re.sub(r'^X',"",ln)
        x=re.sub(r'Y.*$','',x)
        x=float(x)/1000
        y=re.sub(r'^X.*Y','',ln)
        y=float(y)/1000
        hole.append({'tool':currentTool,'x':x,'y':y})

File.close()

outstring="{"+"\"tools\":{\n"
first=1
for t in tool:
    if not(first):
        outstring=outstring+",\n"
    else:
        first=0
    outstring=outstring+"\t\""+t['id']+"\":"+str(t['size'])+""
outstring=outstring+"\n\t},\n\"holes\":[\n"

first=1
for h in hole:
    if not(first):
        outstring=outstring+",\n"
    else:
        first=0
    outstring=outstring+"\t{\"tool\":\""+h['tool']+"\","
    outstring=outstring+"\"x\":"+str(h['x'])+",\"y\":"+str(h['y'])+"}"
    
outstring=outstring+"\n\t]\n"
    
outstring=outstring+"}\n"
if (args.outfile):
    args.outfile.write(outstring)
    args.outfile.close()
else:
    print (outstring)
