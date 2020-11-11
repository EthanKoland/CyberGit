def translate(startLetters, endLetters, spot):
    #find the letter at (spot) in the startLetters string.
    #find the location of the letter in the endLetters string.
    sp = starting[spot]
    loc = endLetters.find(sp)
    return loc


def rotate(alphabet):
    #move the first letter of the alphabet to the end
    #shift all the letters
    alphabet = alphabet[1:] + alphabet[0]
    return alphabet #this has been rotated


def main():
    alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"

    # get a message from the user


    message = "HELLO"
    letter = message[0]

    # Find location of letter in alphabet
    pos = alpha.find(letter)

    #pass this letter through rotor1
    pos = translate(alpha, rotor1, pos) #starting, ending, current position


    #Reflector
    pos = translate(alpha, reflectorA, pos)

    ### Now go back through in the reverse order

    pos = translate(rotor1, alpha, pos)

    #Translate back from position to a letter
    letter = alpha[pos]

    # Now that we have been through one pass, adjust any of the rotors that need to be rotated.
    rotor1 = rotate(rotor1)

    
    print(letter) #This one letter has been encoded


#_______________________________________________________________________________________________________#

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1
    for char in message:
        pos = alpha.find(char)
        freq[pos] = freq[pos] + 1


    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.
    for i in range(len(alpha)):
        print(alpha[i], freq[i])


    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main1():
    msg = input("Enter a message: ")
    countLetters(msg)

main1()