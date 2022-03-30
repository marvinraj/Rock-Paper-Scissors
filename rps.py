import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors'] #this!

while True:
    user_input = input('Type rock/paper/scissors or Q to quit: ').lower()
    if user_input == 'q':
        quit() #this!
    if user_input not in ['rock', 'paper', 'scissors']: #this
        continue #this

    random_number = random.randint(0,2) # this!
    computer_pick = options[random_number]
    print('Computer picked ' + computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print('you won!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('you won!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('you won!')
        user_wins += 1
    else:
        print('You lost!')
        computer_wins += 1 

    
print('You won', user_wins, "times")
print('Computer won', computer_wins, 'times')
print('Goodbye!')