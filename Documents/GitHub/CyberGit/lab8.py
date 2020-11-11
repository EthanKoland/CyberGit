import os

os.chdir("C:/Users/ethan/Documents/GitHub/Cyber 2908/Labs")
print(os.getcwd())

names = open("names.txt", "r")
inp = []
for line in names:
    inp.append(line)

names.close()

out = []
for line in inp:
    words = line.split()
    t = ""
    for i in range(len(words)):

        if(i == 0 or i == 1):
            t = t + words[i] + ", "
        elif(i == 2):
            temp = ""
            temp = words[0][0]
            if(len(words[1]) < 5):
                temp += words[1] + "X"
            else:
                temp += words[1]
            temp += words[3][8:] + ", "
            t += temp
        elif(i == 4):
            temp = words[6][:3] + "-"
            if(words[5] == "Freshman"):
                temp += "FR\n"
            elif(words[5] == "Junior"):
                temp += "JR\n"
            elif(words[5] == "Sophomore"):
                temp += "SO\n"
            elif(words[5] == "Senior"):
                temp += "SR\n"
            t += temp
    out.append(t)
outstr = ""
for i in out:
    outstr += i


outtext = open("students.csv", "w") 
outtext.write(outstr)           

outtext.close()