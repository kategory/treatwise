import re

def getFirstWord(sentence):
    """
    This function takes a sentence as input and returns the first word in the sentence.
    
    Parameters:
    sentence (str): The input sentence from which to extract the first word.
    
    Returns:
    str: The first word in the sentence.

    If the sentence is empty or contains no words, it returns an empty string.
    """
    # Split the sentence into words/token using whitespace as the delimiter
    words = sentence.split()
    
    # Check if there are any words in the list
    if words:
        # Return the f  irst word
        return words[0]
    else:
        # Return an empty string if there are no words
        return ""



#Laura's Copilot implementation of getFirstWord function using regex and without regex:

def getFirstWordWithRegex(sentence):
    match = re.search(r"\S+", sentence)
    return match.group(0) if match else ""



def getFirstWordWithoutRegex(sentence):
    start = 0

    while start < len(sentence) and sentence[start].isspace():
        start += 1

    end = start
    while end < len(sentence) and not sentence[end].isspace():
        end += 1

    return sentence[start:end]

    
# incrementByStandard    
standardIncrement = 1
def incrementByStandard( x ):
        return 0 if x == 0 else 2*(x + standardIncrement)


    

