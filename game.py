#winning rules are as follows
# paper vs rock = paper wins
# rock vs scissor = rock wins
# scissor vs paper = scissor wins
# rock vs lizard = rock wins
#  lizard vs spock = lizard wins
# spock vs scissor = spock wins
# scissor vs lizard = scissor wins
# lizard vs paper = lizard
# paper vs spock = paper wins
# spock vs rock = spock wins

import random
l=["rock","paper","scissor","lizard","spock"]
u_count=0
c_count=0
while True:
    pl=int(input('''
                         GAME START 
                         1 PLAY
                         2 EXIT
                         '''))
    if pl==1:
        for a in range(1,6):
            u_input=int(input('''
                                1 rock
                                2 paper
                                3 scissor
                                4 lizard
                                5 spock
                                '''))
            if u_input==1:
                u_choice="rock"
            elif u_input==2:
                u_choice="paper"
            elif u_input==3:
                u_choice="scissor"
            elif u_input==4:
                u_choice="lizard"
            elif u_input==5:
                u_choice="spock"
            cp_choice=random.choice(l)

            if cp_choice==u_choice:
                print("computer value",cp_choice)
                print("user choice",u_choice)
                print("GAME DRAW")
                u_count=u_count+1
                c_count=c_count+1
            elif (u_choice=="paper" and cp_choice=="rock") or (u_choice=="rock" and cp_choice=="scissor") or (u_choice=="scissor" and cp_choice=="paper") or (u_choice=="rock" and cp_choice=="lizard") or (u_choice=="lizard" and cp_choice=="spock") or (u_choice=="spock" and cp_choice=="scissor") or (u_choice=="scissor" and cp_choice=="lizard") or (u_choice=="lizard" and cp_choice=="paper") or (u_choice=="paper" and cp_choice=="spock") or (u_choice=="spock" and cp_choice=="rock"):
                print("computer valur",cp_choice)
                print("user value",u_choice)
                print("you win")
                u_count=u_count+1
            else:
                print("computer value",cp_choice)
                print("user value", u_choice)
                print("you lose")
                c_count=c_count+1

                if u_count==c_count:
                    print("FINAL GAME DRAW")
                    print("user score",u_choice)
                    print("computer score",cp_choice)
                elif u_count>c_count:
                    print("you win the game")
                    print("user score",u_count)
                    print("computer score",c_count)
                else:
                    print("computer win the game",)
                    print("user score",u_count)
                    print("computer score",c_count)

    else:
        break



