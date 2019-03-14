def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    for i in range(0, len(word)):
        if (len(word)-i) => 6:
            if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
               return True
        else:
            return False   

if __name__ == '__main__':
    # Question 1
    param1 = 'fgaabbccgh'
    return_value = trifeca(param1)
    print(f"Question 1 solution: {return_value}")