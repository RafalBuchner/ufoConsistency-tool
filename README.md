# UFO Consistency-tool
Type production tool that suppose to help in analyse data stored inside ufo files.
It prints data in MarkDown syntax which provide clear, easy to read. edit and share text.
It check the different information in two stages:
1. it runs “Single font tests”, to print out any problems that occurs in single ufo
2. after it, if user fed 'UFO Consistency-tool' script with more than one ufo file it runs “Multiple font tests”, which compares different data between given UFO files

*This project is in very early stages of development, so don't get your hopes up*
---
## Usage:
Check if it works
In terminal go to the UFO Consistency-tool directory, run:

`python UFO-Consistency-tool.py -v`

To see availble commands run:

`python UFO-Consistency-tool.py -h`

### Test one file:

If you want to test one UFO file, then you can pass it as an argument to the script:

In terminal go to the UFO Consistency-tool directory
run:

`python UFO-Consistency-tool.py -n PATH_TO_MY_UFO_FILE/myUfoName.ufo `

### Test more than one file:
move copy of your ufo files to the new directory. Name the directory however you want.

In terminal go to the UFO Consistency-tool directory
run:

`python UFO-Consistency-tool.py -n PATH_TO_MY_DIRECORY/`


---
TODO:
 - Work a bit on file structure
     - Divide `DOCS/FamilyInfo.py` into separate files, so tests and application’s operations won’t be in one python file
     - Learn more about packages :)
 - DOCSRINGS
 - Work on language in the strings


For now:
Single font tests:
 - TODO: CHECK DATA INTEGRITY WITHIN SINGLE UFO FILE
   - IF NECESSARY FILES ARE AVAILABLE ETC
 - TODO check nameID 3 (copyright)
 - TODO check nameID 4 (full name, space separated, only ascii)
 - check nameID6
 - TODO: check if PSfontName is built from familyName and styleName


Multiple fonts tests:
 - font names consistency across family
 - style names consistency across family
 - glyph names consistency across family
 - kerning pairs names consistency across family
 - kerning pairs names consistency across family\n


### this tool depends on following python packages:
```markdown
fontparts
```

```
version: 0.001
name: UFO Consistency Tool
author: Rafał Buchner
date: 03/2018
licence type: MIT
```
