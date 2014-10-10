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
from unidecode import unidecode

def main(File):
    """
    Open the file passed in argument.
    Return in the standard output the text with the special characters
    replaced by ASCII ones.
    """
    fobj = open(File, 'r')
    TxtSpe = fobj.read()
    fobj.close()

    # The unidecode package needs a unicode string.
    # First decode the texte encoded in UTF-8.
    # Then apply the unidecode function that converts it to ASCII with good matches for special characters.
    TxtAsc = unidecode(TxtSpe.decode('utf_8'))
    print(TxtAsc)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1]) # sys.argv[0]=Name of the script, sys.argv[1]= 1st argument
    else:
        print("No Argument. Please pass a filename.")
