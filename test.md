
 [**FATAL ERROR**]> `command like:'-h' doesn't exist`

_______TEST_______

```
version: 0.001
name: UFO Consistency Tool
author: Rafał Buchner
date: 03/2018
licence type: MIT
```
[github link](https://github.com/RafalBuchner/ufoConsistency-tool)
#### Ufo-test-tool: Name Test
---
# Single font tests:
```
 - font `#1` from total `22`
 - font `#2` from total `22`
 - font `#3` from total `22`
 - font `#4` from total `22`

 [**CONSIDER**]> **PostscriptFontNameERROR**: could be a wrong **Postscript Font Name** *'SourceSans_Black'* ( No Separation or separated without the dashes)

\\\\\\\\ *FILE NAME: SourceSans_Black.ufo*

            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic
 - font `#5` from total `22`
 - font `#6` from total `22`
 - font `#7` from total `22`
 - font `#8` from total `22`
 - font `#9` from total `22`
 - font `#10` from total `22`
 - font `#11` from total `22`
 - font `#12` from total `22`
 - font `#13` from total `22`
 - font `#14` from total `22`
 - font `#15` from total `22`
 - font `#16` from total `22`

 [**CONSIDER**]> **PostscriptFontNameERROR**: could be a wrong **Postscript Font Name** *'SourceCode_ExtraLight'* ( No Separation or separated without the dashes)

\\\\\\\\ *FILE NAME: SourceCode_ExtraLight.ufo*

            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic
 - font `#17` from total `22`
 - font `#18` from total `22`

 [**WARNING**]> **FamilyNameERROR** > nameID 1: Ufo without Family Name

\\\\\\\\ *FILE NAME: Untitled copy.ufo*

 [**WARNING**]> **StyleNameERROR** > nameID 1: Ufo without Style Name (if absent then Name ID 2 () is considered to be the typographic style name)

\\\\\\\\ *FILE NAME: Untitled copy.ufo*
 - font `#19` from total `22`
 - font `#20` from total `22`
 - font `#21` from total `22`

 [**CONSIDER**]> **PostscriptFontNameERROR**: could be a wrong **Postscript Font Name** *'Ariļas~ń'* ( No Separation or separated without the dashes)

\\\\\\\\ *FILE NAME: Untitled.ufo*

            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic
 - font `#22` from total `22`

 [**CONSIDER**]> **PostscriptFontNameERROR**: could be a wrong **Postscript Font Name** *'SourceCode_Black'* ( No Separation or separated without the dashes)

\\\\\\\\ *FILE NAME: SourceCode_Black.ufo*

            Common practice: FamilyName-StyleName | for italic: FamilyName-StyleNameItalic

## Summary

> - 6 - number of different family names

> - 22 - number of different style names

# Multiple fonts tests:
 TODO: 
 - font names consistency across family
 - style names consisency across family
 - glyph names consistency across family
 - kerning pairs names consisency across family
 - kerning pairs names consisency across family

### Structure:
|        FAMILY NAME: | Source Sans Variable |                Gamer |          Source Code |               ZigZag |               Ariiba |                 None | 
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            style #0 |               Italic |                 thin |         Black Italic |             bold_con |              Regular |                 None | 
|            style #1 |                Roman |                  400 |    ExtraLight Italic |              reg_con |                      |                      | 
|            style #2 |                Black |                thick |              Regular |              bold_ex |                      |                      | 
|            style #3 |         Black Italic |               medium |               Italic |               reg_ex |                      |                      | 
|            style #4 |                      |                  200 |           ExtraLight |                      |                      |                      | 
|            style #5 |                      |                  800 |                Black |                      |                      |                      | 

# UFO Consistency Tool HELP
---

`-hmd` - Help formated for MarkDown output.
`-h`   - Help formated for terminal output.
`-v`   - Prints out version number and other information about UFO Consistency Tool.
`-n`   - Name Test, that prints out the analize of naming in given UFO files.

# UFO Consistency Tool HELP
---
|                                                                    command |                                                                 description | 
|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                     `-hmd` |                                          Help formated for MarkDown output. | 
|                                                                       `-h` |                                          Help formated for terminal output. | 
|                                                                       `-v` | Prints out version number and other information about UFO Consistency Tool. | 
|                                                                         -n |        Name Test, that prints out the analize of naming in given UFO files. | 
