#Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

import random

print("Snake, Water and Gun is a variation of the children's game rock-paper-scissors where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.")

cc=0
cp=0
while True:
    p=input("Enter snake/water/gun: ")
    a=random.randint(0,2)
    if a==0:
        c='snake'
        print(f"computer choses - {c}")
    elif a==1:
        c='water'
        print(f"computer choses - {c}")
    else:
        c='gun'
        print(f"computer choses - {c}")
    if c==p:
        pass
    elif p=='snake' and c=='water':
        cp+=1
    elif p=='snake' and c=='gun':
        cc+=1
    elif p=='water' and c=='snake':
        cc+=1
    elif p=='water' and c=='gun':
        cp+=1
    elif p=='gun' and c=='snake':
        cp+=1
    elif p=='gun' and c=='water':
        cc+=1
    print(f"Player points: {cp}")
    print(f"Computer points: {cc}")
    if cc==5:
        print("Computer wins")
    elif cp==5:
        print("Player wins")
    else:
        continue
        