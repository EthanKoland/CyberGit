import os
import os.path
from os import path, write
import winsound
import random
import shutil

def main():
    
    if((path.exists("drone.py") == False)):
        f = open('drone.py', "w")
        f.write("import winsound\nimportrandom\ndef beep():\n\twinsound.Beep(random.randint(250, 5000), random.randint(500, 5000))\nbeep()")
        f.close()


    #effect the number of time that the drone program will be ran
    counter = 100
    
    for i in range(counter):
        n = createName()
        shutil.copy("drone.py", n)
        #DO NOT uncomment line unless you want the code to beep
        exec(open(n).read())

def createName():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    n = random.randint(1,10)
    s = ""
    for i in range(n):
        ind = random.randint(0, len(alpha))
        s += alpha[ind - 1]
    s += ".py"
    return s

def beep():
    f = random.randint(250, 5000)
    frequency = f  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(f, 1000)

main()
