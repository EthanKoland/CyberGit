import random
import datetime

#degrees
def degrees():
    t = int(input('put in a value'))
    t = t * 9
    t = t / 5
    t += 32
    print(t)

#RPS
def rps():
    uc = input('Enter R or P or S')
    uc = uc.upper()
    if(uc == 'P'):
        uc = 0
        blah(uc)
        
    elif (uc == 'S'):
        uc = 1
        blah(uc)
    elif (uc == 'R'):
        uc = 2
        blah(uc)
    else:
        print('errir')

def blah(uc):
    cc = random.randint(0,2)
    
    if(uc == cc):
        print('tie')
    elif (uc == 2 and cc == 0):
        print('lose')
    elif (uc == 0 and cc == 2):
        print('win')
    elif (uc < cc):
        print('lose')
    elif (uc > cc):
        print('win')
#pi needs stop watch 
def pi():
    ct = datetime.datetime.now()
    n = int(input('pick a number between 1-10'))
    pi = 0
    i = 0
    sm = ct.microsecond
    ss = ct.second
    cp = int(3.14159265359 * 10**n)
    while(int(pi * 10**n) != cp):
        pi += ((-1)**i * 4/(i*2 + 1))
        i += 1
    fs = ct.second
    fm = ct.microsecond
    print(pi)
    #calc differing values

    print(ss, sm, fs, fm )
    
pi()
    
    
    
        
    
    
