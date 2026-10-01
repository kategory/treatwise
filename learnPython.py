def getFirstWord(sentence):
    """
    This function takes a sentence as input and returns the first word in the sentence.
    
    Parameters:
    sentence (str): The input sentence from which to extract the first word.
    
    Returns:
    str: The first word in the sentence.

    If the sentence is empty or contains no words, it returns an empty string.
    """
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    
    # Check if there are any words in the list
    if words:
        # Return the f  irst word
        return words[0]
    else:
        # Return an empty string if there are no words
        return ""

