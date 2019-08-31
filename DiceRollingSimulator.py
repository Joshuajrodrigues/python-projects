import random
import sys

def dice(roll):
    print('The roll is ...' + str(roll))
while True:
    print('Type \'roll\' to roll dice, type \'exit\' to exit')

    roll_in = input()

    if roll_in =='exit':
        sys.exit()
    elif:
        r= random.randint(1,6)
        dice(r)
    else:
        print('Invalid Input')



