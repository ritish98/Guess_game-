import random
import time
number = random.randint(1,2)
print('A number has been generated between 1-2')


num = input('Guess the number? ')

if not num.isnumeric():
    print('invalid entry, ' + num + ' is not a number, terminating program...')
    exit()
    
if  int(num) == number :
    print("it's correct")  
elif int(num) <1 or int(num)>10  :
    print('invalid entry,choose between 1-10 only')
else  :
    print('sorry, try  again')

    