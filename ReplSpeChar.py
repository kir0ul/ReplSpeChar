#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Replace special characters from a text file with ASCII characters.

Typical use in a terminal:
python ReplCarSpeParAscii.py SourceFile > FileWithoutSpecialCharacters

Need the unidecode package that can be installed with:
pip install unidecode
"""

import sys

def ReplSpeChar(File, enc='utf-8'):
    """
    Open the file passed in argument.
    Return in the standard output the text with the special characters
    replaced by ASCII ones.

    The argument "enc" is the codec used to encode the file.
    Default encoding is 'utf_8'.
    Standard codecs can be found at the following address:
    https://docs.python.org/3.6/library/codecs.html#standard-encodings
    """
    try:
        from unidecode import unidecode
    except ImportError:
        print("Package unidecode not found.")
        print("You can install it with:\npip install unidecode")
        sys.exit()

    with open(File, encoding=enc, mode='r') as fobj:
        TxtSpe = fobj.read()

    # The unidecode package needs a unicode string.
    # First decode the texte encoded with the "enc" codec.
    # Then apply the unidecode function that converts it to ASCII with good matches for special characters.
    TxtAsc = unidecode(TxtSpe)
    return TxtAsc

if __name__ == "__main__":
    # sys.argv[0]=Name of the script, sys.argv[1]= 1st argument
    if len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            TxtAsc = ReplSpeChar(sys.argv[1])
        elif len(sys.argv) == 3:
            TxtAsc = ReplSpeChar(sys.argv[1], sys.argv[2])
        print(TxtAsc)
    else:
        print("No Argument passed.\nPlease pass a filename.")
