from learnPython import getFirstWord

def helperFunction():
    # This is a helper function that is not a test case.
    pass

def test_getFirstWord_returnsFirstWordFromMultipleWords():
    inputSentence = "Hello world from Treatwise"
    expectedResult = "Hello"
    assert getFirstWord(inputSentence) == expectedResult


def test_getFirstWord_returnsWordForSingleWord():
    inputSentence = "Treatwise"
    expectedResult = "Treatwise"
    assert getFirstWord(inputSentence) == expectedResult


def test_getFirstWord_returnsEmptyStringForEmptyInput():
    inputSentence = ""
    expectedResult = ""
    assert getFirstWord(inputSentence) == expectedResult


def test_getFirstWord_returnsEmptyStringForWhitespaceOnly():
    inputSentence = "   \t \n  "
    expectedResult = ""
    assert getFirstWord(inputSentence) == expectedResult


def test_getFirstWord_handlesLeadingAndTrailingWhitespace():
    inputSentence = "   Python is fun   "
    expectedResult = "Python"
    assert getFirstWord(inputSentence) == expectedResult

def test_getFirstWord_handlesLongUnicodeStrings():
    inputSentence = "龍 𪚥"
    expectedResult = "龍"
    assert getFirstWord(inputSentence) == expectedResult

'''
1. Ein klassisches Zeichen (3 Bytes)
Hier ist das traditionelle Zeichen für Drache (Lóng), das extrem oft auf chinesischen Familiensiegeln (Inkan/Hanko) verwendet wird:

龍
Unicode: U+9F8D

UTF-8 Hex: E9 BE 8D (Genau 3 Bytes)

2. Ein historisches Extrem-Zeichen (4 Bytes)
Wenn du testen willst, ob dein System auch mit der sogenannten Supplementary Ideographic Plane (den ganz seltenen, erweiterten Unicode-Zeichen) klarkommt, nimm dieses hier. Es besteht aus vier Drachen und bedeutet so viel wie "geschwätzig":

𪚥
Unicode: U+2A6A5

UTF-8 Hex: F0 AA 9A A5 (Genau 4 Bytes)

'''