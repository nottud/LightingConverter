# LightingConverter
Allows conversion of a lighting file into XS code allowing use in random maps or scenarios without the need of external lighting files.

## Prerequisite
This program uses Python so please install it before attempting to use this program.

## How to use
Open the command prompt in location of the program and provide the following:
```
python LightingConverter.py lightingfiletoconvert.lgt
```
This will dump the code out to the console screen in two parts which you can then paste into the XS code snippet trigger pasting both parts one after the other either into the same XS code snippet or seperate one. The reason for splitting into two parts is due to a character limit on pasting in Age of Mythology so I splitting the output to make the pasting easier.

The trigger code when run should then set the lighting to the same as what the lighting file is.

## Limitations
* Lightings using LUT files are not supported and not something I can support. However hardly any existing lightings use them and there's no easy way to make them. The much easier built in colour grading options however are fully supported.
* God powers that change the lighting will lose the lighting because it is not a proper lighting. I have however found a workaround: Loop setting the lighting followed by a trigger effect applying the default lighting with a super long fade time like 999999.0. This will maintain your lighting and the setting of the standard lighting with the long fade cancels the faded lighting by the god power.
