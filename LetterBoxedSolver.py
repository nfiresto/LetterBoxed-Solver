import json

# This function takes in two adjacent letters in a word and the box given in the day's puzzle
# The function then checks if the adjacent letters are not on the same side in the box.
# It returns True or False
def SideCheck(letter1, letter2, box):
    Top = box['Top']
    Bottom = box['Bottom']
    Left = box['Left']
    Right = box['Right']
    if letter1 in Top:
        if letter2 in Bottom:
            return True
        if letter2 in Left:
            return True
        elif letter2 in Right:
            return True
        else:
            return False
    elif letter1 in Bottom:
        if letter2 in Top:
            return True
        if letter2 in Left:
            return True
        elif letter2 in Right:
            return True
        else:
            return False
    elif letter1 in Right:
        if letter2 in Bottom:
            return True
        if letter2 in Left:
            return True
        elif letter2 in Top:
            return True
        else:
            return False
    elif letter1 in Left:
        if letter2 in Bottom:
            return True
        if letter2 in Top:
            return True
        elif letter2 in Right:
            return True
        else:
            return False
    else:
        return False

# This function takes in a word and the day's box
# This function checks if a word can be used in the box
# It outputs True or False
def WordCheck(word, box):
    i = 1
    while i < len(word):
        if i == len(word)-1:
            return True
        else:
            if SideCheck(word[i], word[i+1], box) == True:
                i += 1
            else:
                return False
    return True

# This function takes in a dictionary of words and the day's box.
# This function loops through words in a dictionary and sees if they work in the box or not. 
# It outputs True or False
def GetWords(dict, box):
    words = []
    for i in dict:
        for j in dict[i]:
            first = i
            first2 = j
            if SideCheck(first, first2[1], box) == True:
                for k in dict[i][j]:
                    if WordCheck(k, box) == True:
                        words.append(k)
    return words

# This function takes in a list of words and the day's box.
# This function generates pairs of words
# It outputs a list of word pairs
def InARow(wordlist, box):
    pairs = []
    for word1 in wordlist:
        for word2 in wordlist:
            if word1 == word2:
                "cool"
            elif word1[0] == word2[-1]:
                pairs.append([word2, word1])
    return pairs

# This function takes in a list of word pairs and the day's box.
# this function checks if the word pairs use all of the letters in the puzzle and solve it.
# it outputs a list of word pairs that solve the puzzle
def AllLetters(pairs, box):
    all = []
    for set in box:
        for letter in box[set]:
            all.append(letter)
    final = []
    for pair in pairs:
        total = 0
        joe = []
        for word in pair:
            for letters in word:
                if letters in all:
                    total += 1
                    if letters not in joe:
                        joe.append(letters)
        if len(joe) == 12:
            final.append(pair)
    return final

# This function has the user input the day's puzzle into the terminal
# It returns the box of the day so other functions can parse it.
def BoxMaker():
    top = input('Top Row Letters: ')
    Top = []
    for letter in top:
        Top.append(letter)
    left = input('Left Column Letters: ')
    Left = []
    for letter in left:
        Left.append(letter)
    right = input('Right Column Letters: ')
    Right = []
    for letter in right:
        Right.append(letter)
    bottom = input('Bottom Row Letters: ')
    Bottom = []
    for letter in bottom:
        Bottom.append(letter)
    Box = {'Top': Top, 'Left': Left, 'Right': Right, 'Bottom': Bottom}
    if len(Box['Top']) != 3 or len(Box['Left']) != 3 or len(Box['Right']) != 3 or len(Box['Bottom']) != 3:
        print('Try Again')
        return
    return Box

# this function takes in a list of word pairs and outputs the one with the most total letters
def BestPair(pairs):
    if len(pairs) == 1:
        pair = pairs[0]
        return pair
    else:
        bestsofar = BestPair(pairs[1:])
        word1 = bestsofar[0]
        word2 = bestsofar[1]
        bestletters = len(word1)+len(word2)
        pair = pairs[0]
        word3 = pair[0]
        word4 = pair[1]
        numletters = len(word3)+len(word4)
        if numletters > bestletters:
            return pair
        else:
            return bestsofar

# This function takes in the best pair and prints it
def PrintBest(pair):
    word1 = pair[0]
    word2 = pair[1]
    bestletters = len(word1)+len(word2)
    print('The Total Number of Letters is', bestletters)
    print('The Best Pair is', pair)

# This function generates a list of words that can be used in the puzzle
# This is a way to check if the words generated are indeed 'real words' according to the internal dictionary the site uses. 
def WordsLeft(pairs):
    newords = []
    for pair in pairs:
        for word in pair:
            if word not in newords:
                newords.append(word)
    return newords

# This function checks a list of words and sees if they are in the 'nytdict.json' file in this repository. 
def CheckNYTDict(words):
    newords = words[:]
    import json
    f = open('nytdict.json')
    nyt = json.load(f)
    z = 0
    y = len(newords)
    while z < y:
        for i in nyt:
            for j in nyt[i]:
                word = newords[z].upper()
                if word == j:
                    newords.remove(newords[z])
                    z -= 1
                    y -= 1
        z += 1
    '''
    print('There are', len(newords),
          'words from final pairs not in the NYT Dictionary')
    print("Those words are", newords)
    '''
    return newords

## This if the function that ties all of the above functions together to solve the puzzle
## It has no inputs and the output is printing a solution to the puzzle

def SolveLetterBoxed():
    box = BoxMaker()
    import json
    f = open('dicts.json')
    dict = json.load(f)
    words = GetWords(dict, box)
    print('There are', len(words), 'words')
    set = []
    for word in words:
        if WordCheck(word, box) == True:
            set.append(word)
    pairs = InARow(set, box)
    final = AllLetters(pairs, box)
    wordsleft = WordsLeft(final)
    CheckNYTDict(wordsleft)
    if len(final) == 1:
        print('There is 1 pair')
    else:
        print('There are', len(final), 'pairs')
    best = BestPair(final)
    PrintBest(best)


SolveLetterBoxed()
