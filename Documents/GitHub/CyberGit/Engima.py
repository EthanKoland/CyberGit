import random
import time


class router():
    def __init__(self):
         self.positions = []
         for i in range(3):
             self.positions.append(random.randint(0, 25))
        self.cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self, n1,n2.n3):
         self.positions = [n1,n2,n3]
        self.cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        
    def outValue(self):
        print(self.positions)

    def updateDial(self):
        self.positions[0] = self.positions[0] + 1
        for i in range(len(self.positions) - 1):
            if(self.positions[i] >= 26):
                self.positions[i] = self.positions[i] % 25
                self.positions[i+1] = self.positions[i+1] + 1
        if(self.positions[len(self.positions)-1] >= 26):
                self.positions[len(self.positions)-1] = self.positions[len(self.positions)-1] % 25
        

#make it so that it can add another dial later



r1 = router()


    
        