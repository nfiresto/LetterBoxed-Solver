def CheckNYTDict(words):
    newords = words[:]
    notinit = []
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
    print('There are', len(newords), 'words not in the NYT Dictionary')
    print("Those words are", newords)
