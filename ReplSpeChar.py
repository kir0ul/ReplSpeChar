#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Replace special characters from text file(s) with ASCII characters.

Typical use in a terminal for one file:
python ReplSpeChar.py SourceFile [encoding] > FileWithoutSpecialCharacters

Typical use in a terminal for a whole folder:
python ReplSpeChar.py FolderName [encoding]

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
    Default encoding is 'utf-8'.
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



def WalkReplSpeChar(path, enc='utf-8'):
    """
    Replace special characters from text files inside the "path" directory
    """
    import os
    import mimetypes as mt

    # import pdb; pdb.set_trace()
    
    # Single file case: print the content of the file without the special characters
    if os.path.isfile(path):
        TxtAsc = ReplSpeChar(path, enc)
        print(TxtAsc)
        return TxtAsc

    # Directory case: replaces each text file by its new version without the special characters
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                fPath = os.path.join(root, f)
                print("Processing file: " + fPath)
                if mt.guess_type(fPath)[0] == 'text/plain':
                    TxtAsc = ReplSpeChar(fPath, enc)
                    with open(fPath, encoding=enc, mode="w") as fobj:
                        fobj.write(TxtAsc)
            
    else:
        print("The passed argument is neither an existing file, nor an existing folder.")
        sys.exit()
        
    

if __name__ == "__main__":
    # sys.argv[0]=Name of the script, sys.argv[1]= 1st argument
    if len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            TxtAsc = WalkReplSpeChar(sys.argv[1], sys.getdefaultencoding())
        elif len(sys.argv) == 3:
            TxtAsc = WalkReplSpeChar(sys.argv[1], sys.argv[2])
    else:
        print("No Argument passed.\nPlease pass a filename.")
