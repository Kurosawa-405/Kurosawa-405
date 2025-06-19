

import random
# Snake, Water, Gun Game

def victory(response1,comp):
    if response1=='snake'and comp=='water':
        return 1
    elif response1=='water'and comp=='snake':
        return -1
    elif response1=='gun'and comp=='water':
        return 1
    elif response1=='water'and comp=='gun':
        return -1
    elif response1 =='snake' and comp=='gun':
        return -1
    elif response1=='0':
        return 0
    else:
        return 0
    
        
n=int(input("Enter the number of rounds you want to play: "))
for i in range(n):
    response1 = input("Player 1, enter your choice (snake, water, gun): ").lower()
    comp=random.choice(['snake', 'water', 'gun']).lower()
    if victory(response1,comp)==1:    
        print("Player 1 wins") 
    elif victory(response1,comp)==-1:  
        print("Player 2 wins")
    else:
        print("It's a tie")
    print("Thank you for playing!")
    if response1 not in ['snake', 'water', 'gun'] or comp not in ['snake', 'water', 'gun']:
        print("Invalid input. Please choose from snake, water, or gun.")


    
   
        