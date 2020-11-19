
import random

#Dice Roll
def diceRoll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('first roll is', dice1, 'second role is', dice2, 'total is ', dice1+dice2)


#Dice Roll 2
def diceRoll2():
    numOfDice = input('how many dice would you like to roll')
    numOfDice = int(numOfDice)
    sideOfDice= input('How many sides would yo ulie to have your dice roll')
    sideOfDice = int(sideOfDice)
    for x in range(numOfDice):
        print('Dice number', x, 'is', random.randint(1,sideOfDice))
    

#Magic 8ball
def magic8ball():
    ans = ['As I see it, yes', 'Ask again later','Better not tell you now.','Cannot predict now','Concentrate and ask again.','Don’t count on it.', 'It is certain', 'It is decidedly so.','Most likely','My reply is no','My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.','Yes','Yes – definitely.','You may rely on it.']
    blah = input("ask a question")
    print(random.choice(ans))

magic8ball()
