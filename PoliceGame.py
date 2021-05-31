
import random

cont='y'

while cont=='y' or cont=='Y':
    
    print('-----------------------')
    print('----- POLICE GAME -----')
    print('-----------------------')
    name=input('\nHello! Welcome to my POLICE GAME! Please tell me your name Inspector! ')
    
    print('\nHey ',name,'! There is a theif who has stolen money from the bank. You are the police inspector in your town.')
    print('\nThere are 6 suspects. They are namely')
    print('\n1. Postman - Wears a cap. Cloth is green. \n2. Doctor - Wears a cap. Cloth is white.\n3. Mason - Wears a cap. Cloth is blue.\n4. Student - Doesn\'t wear a cap. Cloth is blue.\n5. Principal - Doesn\'t wear a cap. Cloth is white.\n6. Shopkeeper - Doesn\'t wear a cap. Cloth is green.')
    print('\nPlease find who is the theif inspector',name,'. Best of luck! You have 3 guesses! ')
    
    theifnum=random.randint(1,6)

    if theifnum==1:
        theif='postman'
        clue1='wears a cap'
        clue2='cloth is green'
    elif theifnum==2:
        theif='doctor'
        clue1='wears a cap'
        clue2='cloth is white'
    elif theifnum==3:
        theif='mason' 
        clue1='wears a cap' 
        clue2='cloth is blue'  
    elif theifnum==4:
        theif='student'
        clue1='doesn\'t wear a cap' 
        clue2='cloth is blue'   
    elif theifnum==5:
        theif='principal'
        clue1='doesn\'t wear a cap'  
        clue2='cloth is white'
    else:
        theif='shopkeeper'
        clue1='doesn\'t wear a cap'  
        clue2='cloth is green'
        
        
    for i in range(1,4):
        
        userinpt=input('\nPlease enter who is the theif :')
        suspect=userinpt.lower()
        
	
        if suspect in ['doctor','postman','mason','student','principal','shopkeeper']:
            if suspect==theif:
                print('\nCongratulations. You have found the theif! Excellent job!')
                print('Thank you ',name,'for saving the town once again!')
                break
            else:
                print('\nNope. He is not the theif. He was at home during the incident. Try again Inspector',name)
                if i==1:
                    print('The first clue is, the theif ',clue1)
                elif i==2:
                    print('The second clue is, the theif\'s ',clue2)
        else:
            print('\nYou have entered an invalid name Inspector',name,'! Please check the spelling and enter again.')
    print('\nTheif was ',theif.upper(),' !!!! Don\'t let him escape again')
    cont=input('\nDo you want to play again? If yes, enter y. If you want to exit, enter any other key.')
    
    