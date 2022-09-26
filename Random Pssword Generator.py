import random

n= int(input('Enter size of password:'))

def passwordGenerator(n):
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number='0123456789'
    special='!@#$%*'

    password=''
   

    for i in range(n):
         l=[ random.choice(lower),random.choice(upper),random.choice(number),random.choice(special)]
         password=password+ random.choice(l)
    
    return password

print('Your password is: ', passwordGenerator(n))


