from json import load
d = open('words_dictionary.json')
dictionary = load(d)
print(len(dictionary))
newd = []
f = open('new_dictionary.json', 'a')
for i in dictionary:
    if len(i) > 5:
        newd.append(i)
print(len(newd))
i = 0
while i < len(newd):
    word = newd[i]
    j = 0
    while j < len(word)-1:
        if word[j] == word[j+1]:
            if word in newd:
                newd.remove(word)
                j = len(word)
        j += 1
    if word in newd:
        f.write(word + '\n')
    i += 1
print(len(newd))
