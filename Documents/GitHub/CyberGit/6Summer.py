alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Create a ceaser cipher
def createCipher(start):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if(type(start) == str):
        start = alpha.find(start)

    text = ""

    for x in range(26):
        text = text + (alpha[(start+x) % 26])
    return text



def ceaser(text):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    cipher = createCipher(3)
    final = ""
    for x in range(len(text)):
        final = final +  cipher[alpha.find(text[x])]
    print(final)
    
def keyDevop(key):
    key = key.upper()
    temp = []
    for x in range(len(key)):
        temp.append(alpha.find(key[x]))
    return temp

def Vige(text, key):
    keyStarts = keyDevop(key)
    final = ""
    keys = []
    for x in keyStarts:
        keys.append(createCipher(x))
    i = 0
    text = text.upper()
    while i < len(text):
        selectCipher = keys[i % (len(key))]
        final = final + selectCipher[alpha.find(text[i])]
        i = i+1
    print(final)
    


    


