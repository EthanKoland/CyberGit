import shutilgit
import winsound
import random

def main():
    n = createName()
    """f = open(n, "w")
    f.write("import winsound \nimport random\ndef beep():\n\tf = random.randint(250, 5000)\n\twinsound.Beep(f, 1000)\ndef createName():\n\talpha=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\"\n\tn = random.randint(1,10)\n\ts = \"\"\n\tfor i in range(n):\n\t\ts += alpha[random.randint(0, len(alpha)) - 1]\n\ts += \".py\"\n\treturn s\ndef main():\n\tn=createName()\n\tf=open(n,\"w\")\n\tf.write(\"\")\n\tf.close()\n\texec(open(n).read())\nmain()")
    f.close()"""
    shutil.copy2("main.py", n)
    if(true):
        beep()
    else:
        pi()


    #do not uncomment this code!!!!
    #exec(open(n).read())

def createName():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    n = random.randint(1,10)
    s = ""
    for i in range(n):
        s += alpha[random.randint(0, len(alpha)) - 1]
    s += ".py"
    return s

def beep():
    f = random.randint(250, 5000)
    frequency = f  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(f, 1000)

def pi():
    i = 0
    pi = 0
    while(true):
        pi += ((-1)**i * 4/(i*2 + 1))
        i += 1



main()

