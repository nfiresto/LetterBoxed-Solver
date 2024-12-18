d=open('words.txt','r')
dict=d.read()
di = dict.split('\n')
word={}
for i in di:
    nest={}
    first = i[0]
    second = i[1]
    if first not in word:
        nest[first+second] = [i]
        word[first] = nest
    elif first+second not in word[first]:
        word[first][first+second]= [i]
    else:
        word[first][first+second].append(i)
words = str(word)
f=open('dicts.json', 'a')
f.write(words)