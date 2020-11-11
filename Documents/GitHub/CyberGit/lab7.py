import math

def isPrime(n):
    if(n == 1 or n == 0):
        return False
    n = int(n)
    lim = int(n/2)
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True
    

def factors(n, df):
    fact = []
    fb = []
    for i in range(1, math.ceil(n/2) + 1):
        if(n%i == 0):
            fact.append(i)
    if(df):
        fact.append(n)
            
    
    return(fact)

    

def lPF(n):
    i = n - 2 
    while i >= 0:
        
        if(n%i == 0 and isPrime(i)):
            print(isPrime(i))
            return i
        i -= 1
    print('error')
        
                            

def palendrom():
    n = 999*999
    while n >= 0:
        if( n == rn(n)):
            return n
        n -= 1
  
   

def rn(n):
    r = 0
    while n >= 1:
        r = 10 * r
        r += n%10
        n = n/10
        n = int(n)
        
    return r

def lP():
    pr = []
    i = 2
    while len(pr) <= 10001:
        if(isPrime(i)):
            pr.append(i)
        i += 1
    return(pr[len(pr)-1])   

def SOP():
    ans = 0
    for i in range(10):
        if(isPrime(i)):
            ans += i
            print(i)
    return ans

def sumOfArray(n):
    ts = 0
    for t in n:
            ts += t
    
    return ts


def ami():
    s = 0
    
    for i in range(10000):
        fact = factors(i, False)
        
        s1 = sumOfArray(fact)
        
        fact = factors(s1, False)
       
        s2 = sumOfArray(fact)
      
        if(s2 == i and s1 != i):
            s += i
    return s
    
def n23():
    s = 0
    abn = []
    num = []
    for i in range(1, 28123):
        if(sumOfArray(factors(i, False)) > i):
            abn.append(i)
    print(abn)
    
    for i in range(28123):
        num.append(i)

    for i in range(len(abn)):
        for t in range(i + 1):
            if((abn[i] + abn[t]) > 28123):
                t = i
            elif((abn[i] + abn[t]) in num):
                num.remove(abn[i] + abn[t])
    print(sumOfArray(num))
    
def n41():
    n = []
    for i in range(100000000, 987654321):
        if(containsNoDups(i)):
            n.append(i)
    
    for i in range(len(n)):
        if(isPrime(n[len(n) - 1 - i])):
            return n[len(n) - 1 - i]
    print('no pimes avaiable')


        
def containsNoDups(i):
    a = [0] * 9
    n = i
    while n > 0:
        t = n%10
        if(a[t-1] > 0):
            return(False)
        else:
            a[t-1] += 1
            n = int(n/10)

    return 
    
def n47():
    
    notfound = False
    n1 = 5
    
    while not(notfound):
        notfound = True
        
        for i in range(4):
            if(aOfPrime(factors(n1 + i, False)) >= 4):
                notfound = notfound and True
            else:
                notfound = False
        n1 += 1
    print("the answer is",n1 - 1 )
        


              

def aOfPrime(n):
    c = 0
    for i in n:
        if(isPrime(i)):
            c += 1
    return c

def n50():
    n = []
    for i in range(1000000):
        if(isPrime(i)):
            n.append(i)
    print(n)
    s = 0
    m = 0
    for i in range(len(n)):
        for t in range(len(n) - i):
            s += n[t + i]
            if(s > 1000000):
                s = 0
                break
        if(isPrime(s)):
            m = max(s, m)
        print(m)
        s = 0
    
    




n50()



    
        




