import random
from RPSModerator import game_Shape, game_Shape_As_String

# Write Code 💻
name = input("\nKaede : What's Your Name -> ")
print(f"\n\nKaede : Welcome To RPS Game {name}.")
print(f"\n\nKaede : Winning Rules Of The RPS Game As Follows: \n\n"
                                +"\nRock Beats Scissors.\n"
                                +"\nScissors Beat Paper.\n"
                                +"\nPaper Beats Rock.\n")

kaede_Choice = random.randint(0,2)

def RPS():
    while True:
        user_Choice = int(input(f"\n\nKaede : Which Game Shape Would You Like To Choose -> \n\n0. Rock\n\n1. Paper\n\n2. Scissor\n\n\n{name} : "))
        print("\n\n----------------------")

        if kaede_Choice == 0 and user_Choice == 0:
            print(f"\n\n{name} Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print("\n\nKaede : It's A Draw.\n")
        
        elif kaede_Choice == 1 and user_Choice == 1:
            print(f"\n\n{name} Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print("\n\nKaede : It's A Draw.\n")
        
        elif kaede_Choice == 2 and user_Choice == 2:
            print(f"\n\n{name} Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print("\n\nKaede : It's A Draw.\n")
        
        
        if kaede_Choice == 1 and user_Choice == 0:
            print(f"\n\n{name} Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print("\n\nKaede : Kaede Wins.\n")
            break
        
        elif kaede_Choice == 0 and user_Choice == 2:
            print(f"\n\n{name} Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print("\n\nKaede : Kaede Wins.\n")
            break

        elif kaede_Choice == 2 and user_Choice == 1:
            print(f"\n\n{name} Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print("\n\nKaede : Kaede Wins.\n")
            break

        if kaede_Choice == 0 and user_Choice == 1:
            print(f"\n\n{name} Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print(f"\n\nKaede : {name} Wins.\n")
            break

        elif kaede_Choice == 2 and user_Choice == 0:
            print(f"\n\n{name} Chose {game_Shape_As_String[0]}.\n\n{game_Shape[0]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print(f"\n\nKaede : {name} Wins.\n")
            break

        elif kaede_Choice == 1 and user_Choice == 2:
            print(f"\n\n{name} Chose {game_Shape_As_String[2]}.\n\n{game_Shape[2]}")
            print(f"\n\nKaede Chose {game_Shape_As_String[1]}.\n\n{game_Shape[1]}")
            print(f"\n\nKaede : {name} Wins.\n")
            break

        if user_Choice >= 3:
            print("\n\nKaede : Invalid Value.\n")


isContinue = True

while isContinue:
    RPS()
    restart_Program = input("\nKaede : Would You Like To Restart The Program? Y/N -> ").lower()
    
    if restart_Program == "y":
        isContinue = True
    
    else:
        isContinue = False
        print(f"\n\nKaede : See You Later {name} ~\n\n")


    
    
    
