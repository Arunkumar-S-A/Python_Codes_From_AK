#ROCK PAPER SCISSORS
def yesorno(n):
    n=input("Valid inputs, 'y' or 'n' : ")
    n=n.upper()
    if n=='Y' or n=='N':
        return n
    else:
        return yesorno(n)
def stnpapsci(n):
    n=input("Valid inputs, 'r' or 'p' or 's' : ")
    n=n.upper()
    if n=='R' or n=='P' or n=='S':
            return n
    else:
        return stnpapsci(n)
import random
r=0
w=0
l=0
dr=0
a=input("Do you wanna play ROCK PAPER SCISSORS ?\n\
Give inputs as,\n\
'y' for YES\n\
'n' for NO\n\
YES or NO ? : ")
a=a.upper()
if a!='Y' and a!='N':
    a=yesorno(a)
while a=='Y':
    print("Let's Play")
    if r==0:
        print("Give inputs as,\n\
'r' for ROCK\n\
's' for SCISSORS and\n\
'p' for PAPER")
    d=input("ROCK, PAPER, SCISSORS ? : ")
    d=d.upper()
    li=['R','P','S']
    if d not in li:
        d=stnpapsci(d)
    if d=='R':
        d='ROCK'
    elif d=='P':
        d='PAPER'
    elif d=='S':
        d='SCISSORS'
    c=random.choice(li)
    if c=='R':
        c='ROCK'
    elif c=='P':
        c='PAPER'
    elif c=='S':
        c='SCISSORS'
    print('YOU :',d)
    print('COMPUTER :',c)
    if d=='ROCK' and c=='SCISSORS':
        print("YOU WIN")
        w+=1
    elif d=='SCISSORS' and c=='PAPER':
        print("YOU WIN")
        w+=1
    elif d=='PAPER' and c=='ROCK':
        print("YOU WIN")
        w+=1
    elif d==c:
        print('DRAW')
        dr+=1
    else:
        print("YOU LOSE")
        l+=1
    r+=1
    a=input("Do you wanna play again? YES or NO :")
    a=a.upper()
    if a!='Y' and a!='N':
        a=yesorno(a)
else:
    if r>0:
        print("SUMMARY :")
        print("Number of rounds played :",r)
        print("Number of rounds YOU WON :",w)
        print("Number of rounds COMPUTER WON:",l)
        print("Number of rounds DRAWED :",dr)
        print("Thanks for playing")
    else:
        print("Thank you")
    
