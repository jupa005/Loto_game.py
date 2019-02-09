from random import *
print('Welcome to loto game!')
print('You will select 7 numbers (1-39).')
print('Try to guess as much correct numbers as you can!')
loto=[]
guess=[]
same=[]
count=0
#This part is for generating 7 random numbers
for i in range(7): 
    a=randint(1,39)
    while a in loto:
        a=randint(1,39)
    loto.append(a)

#This is part when you enter your numbers
for i in range(7):
    b=int(input('Enter your number: '))
    while b<1 or b>39:
        print('Your number is not in correct range (1-39)!')
        b=int(input('Enter your number: '))
    while b in guess:
        print('You have already chosen this number!')
        b=int(input('Enter your number: '))
    guess.append(b)
    if b in loto:
        count+=1
        same.append(b)

print('Loto numbers: ')
print(loto)
print('Your numbers: ')
print(guess)
print('Number of correct numbers: ')
print(count)
print('The umbers you hit: ')
print(same)
if count=7:
    print('CONGRATULATIONS!!! LOTO!!!!')
        

    
