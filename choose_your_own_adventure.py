name = input('Type your Name: ')
print("Welcome", name, "to this adventurew")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across it. Which way would you like to go? Type walk to walk around type swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across the river and got eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
        
    else:
        print("Not a Valid option. You lose.")             

elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it? Type cross to cross the bridge or type back to go back: ")
    
    if answer == "back":
        print("You go back to the main road. you proceed no further you coward.")
    
    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them? Type yes or no: ")
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold.  You WIN!")
            
        elif answer == "no":
            print("You ignore the stranger and they are offended and you Lose!")
            
        else:
        print("Not a Valid option. You lose.")
        
    else:
        print("Not a Valid option. You lose.")
    
else:
    print("Not a Valid option. You lose.")   
    
print("Thank you for trying" ,name"!")