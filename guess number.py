import random as rd

print('Make a guess 3 times: \n')

guess_number= rd.randint(1,10)   


for i in range(3):    

    user_number=int(input('Guess a number between 1 and 10: \n'))

    if user_number==guess_number:
        print('Congratulations, you won!')
        break

    else:
        print('You failed. Better luck next time')
        
print('\n')
print('The correct number was: ', guess_number)