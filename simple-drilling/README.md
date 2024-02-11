# Simple drilling
Here are two python scripts to manage drilling with swith a drill or with a mill
## json2gcode.py  
To convert Translate Excellon .xln files from EAGLE PCB to a standard description JSON file

```
usage: xln2json.py [-h] [-w OUTFILE] filename

Translate Excellon .xln files to standard JSON description

positional arguments:
  filename    xln (text) file

options:
  -h, --help  show this help message and exit
  -w OUTFILE  the output file
```

## xln2json.py
To convert a standatd JSON file to a gcode file ready to be used with candle
```
usage: json2gcode.py [-h] [-w OUTFILE] filename

Translate JSON standard files files to gcode for CNC3018

positional arguments:
  filename    xln (text) file

options:
  -h, --help  show this help message and exit
  -w OUTFILE  the output file
```
