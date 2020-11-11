import datetime

#Magic 8ball
def magic8ball():
    ans = ['As I see it, yes', 'Ask again later','Better not tell you now.','Cannot predict now','Concentrate and ask again.','Don’t count on it.', 'It is certain', 'It is decidedly so.','Most likely','My reply is no','My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.','Yes','Yes – definitely.','You may rely on it.']
    blah = input("ask a question")
    print(random.choice(ans))

#Time calulator
def timeCalc():
    #d = input('How Many days ')
    h= int(input('How Many hours '))
    m = int(input('How Many minutes '))
   # s = input('How Many days ')
    ct = datetime.datetime.now()
    tm = ct.minute
    th = ct.hour
    m = tm + m
    if( m >= 60):
       h += 1
       m = m % 60
    h = ((h + th)%12) 
    if(h == 0):
        h = 12
    print('the time will be',h,':',m)

timeCalc()


