import random
#Dice roll
def diceroll():
    freq = []
    runs = 10000
    percent = []
    for i in range(12):
        freq.append(0)

    for i in range(runs):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        dt = d1 + d2
        
        freq[dt-1] = freq[dt-1] + 1
        
    for i in freq:
        percent.append(i/runs)
    print(freq, "\n", percent)

#__________________________________________________________________#
#word count
def wc():
    textFile = open("g.txt", 'r')
    lc = 0
    cc = 0
    sc = 0

    for line in textFile:
        lc += 1
        cc += len(line)
        for char in line:
            if(char == " " or char == "—"):
                sc += 1
    print('line count', lc, "word count", sc + 1, "char Count", cc)

#____________________________________________________________________#
# word freq
def wf():
    textFile = open("g.txt", 'r')
    words = {}
    for line in textFile:
        ws = line.split()
        for w in ws:
            if(words.get(w, "-1") != '-1'):
                words.update({w:words.get(w)+1})
            else:
                words.update({w:1})

    print(words)

wf()
            


    