import random as ra
for i in range (1):
    global no 
    no= ra.randint(1,9)
a1 = int(input(print("Guess the no b/w 1 to 9 \n" )))
if a1==no:
    print("Yay! You guessed it right, it is %d"%(a1))
else:
    a2=int(input(print("You guessed it wrong. Don\'t worry you have  two  more tries \n")))
    if a2==no:
        print("Yay! You guessed it right, it is %d"%(a2))        
    else:
        a3=int(input(print("You guessed it wrong. Don\'t worry you have  one more try \n")))
        if a3==no:
            print("Yay! You guessed it right, it is %d"%(a3))            
        else:
            print("You guessed it wrong. You have lost all your chances")


    
