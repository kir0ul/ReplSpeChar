# ReplSpeChar #

Simple Python script replacing special characters from a text file using the [Unidecode](https://pypi.python.org/pypi/Unidecode) package.

To try it:

```
python ReplSpeChar ExampleForTest.txt
```

The codec used to encode your file can be optionally passed as one of the [standard codecs](https://docs.python.org/3.6/library/codecs.html#standard-encodings) with:
```
python ReplSpeChar FileToRemoveSpecialCharacters CodecUsed
```
Otherwise, _utf_8_ will be assumed.