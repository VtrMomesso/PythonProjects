# Milestone Activity: Adventure Game.

# by Victor dos Santos

print("Welcome to the Game: How keep the ball?")
name = input("Before more explanation, please tell me your name: ")
name = name.capitalize()

print()
print(f"Now {name}, I will explain the rulers: " )
print("How keep the ball in the end of the match win. ")
print("You have three turns making choices, to win this game. ")
print("Your opponet is the best in this game, so be cautius. ")
print("The local is a playground with 100 square metres and ")
print("Trere are some obstacules, like slide, seesaw and climbing frame. ")
print("So, let's beggin the game!")
print("_______________________________________________________________")
print()


print("You both are behind the line, waiting the star time, the ball is almost 20 steps of you in the floor.\n ")
first_choice = input("What is the first thing that you want to do? WALK, RUN or WAIT: \n")
if first_choice.lower() == "walk":
    print("Your opponent runs so fast and didn't understant why you are walking until the ball. He arrives close the ball and take it with the both hands, then he goes until the climbing frame and stayed behind it with the ball \n ")
    second_choice = input("What you chose to do, RUN AROUND the climbing frame, WALK CLOSER your opponent or CLIMB UP in the climbing frame? \n ")
    print()
    if second_choice.lower() == "run around":
        print("You can run as fast as your opponent but you can't touch the ball and your opponent looks like a little tired. \n ")
        third_choice = input("You can continuing RUNING, JUMP or THINK: \n ")
        print()
        if third_choice.lower() == "runing":
            print("You can get closer because your opponent is tired, but you are tired also and you don't give up, your can touch the ball, therefore you don't have energy because you were running all the time, while sometimes your opponent was stoped and brething normally. So you can't take the ball, you lose the match. \n ")
        elif third_choice.lower() == "jump":
            print("You jumped like a gazelle, and hit your chest in the floor, but you can touch your opponent's feet and he fell and the ball flew away of his hands, and you belive that was your chance, and you put in your feet tried to run, but the opponent hold on your legs making you fell, and you can't breath at that moment. \n ")
        else:
            print("You lost a lot of time tinking and you lose the game. \n ")


    elif second_choice.lower() == "walk closer":
        print("Your opponent watch you walking closer, he doesn't understand yet what your strategy is, and thinking about this, he isn't moving and your closer than expected.\n ")
        third_choice = input("Now you are close enough to HOLD THE OPPONENT or TRY HOLD THE BALL. \n ")
        if  third_choice.lower() == "hold the opponent":
            print("You hold your opponent with a intimidate look, and your opponent was frozen withowt reaction, and you can take off his ball. The opponent try to move again but when he goes close to the ball there is no enough time and his was desapinted with heself, because he loses the game. Congratulations you Win! \n ")
        elif third_choice.lower() == "try hold the ball":
            print("Your opponent try to resist and you hit the ball and it fly away and go down close to you. You hold that like your life depending this and the time is over. In this way you win the game! Congratulations! \n ")
        else:
            print("This oppitions makes you lose the game, because you don't understand your options. \n ")

    elif second_choice.lower() == "climb up":
        print("You show a great agility in the climbing flame, but as fast as you climb up your opponent go to the slide.\n ")
        third_choice = input("You can JUMP to though the slide or you can RUN \n ")
        if  third_choice.lower() == "jump":
            print("Your jump was like a roquet, you fell through the slide and was hurting your belly in the floor, but your don't give up because you are so close to your opponent, He runs so fast and your lost looks like close. The time is over and you aren't with the ball.\n ")
        elif third_choice.lower() == "run":
            print("You ruan as fast as you can and the opponent looking at you stumble in his own feet and fell losing the ball. In the exactly moment that you take the ball the time is over and you win this match, congratulations!\n ")
        else:    
            print("You don't make a good choice and lose the match because this choice. \n")

elif first_choice.lower() == "run":
    print("You run as fast as your opponent and you take the ball at same time, you put the right hand in the ball and your the left hand and you are fighting. \n")
    second_choice = input("You can PULL the ball to you with the right hand or PUSH your opponent with the another hand. \n ")
    if second_choice.lower() == "pull":
        print("You pull the ball close to you but before you can hold it with the both hand your opponent slepped it, and the ball move on in your front and your opponent revice a litte advantage \n")
        print()
        third_choice = input("You can PULL your opponent our try JUMP until the ball. \n ")
        if third_choice.lower() == "pull":
            print("You pull your opponent and pass in his front and achive the ball, with a shot time to finish the game, you keep the ball some seconds more and own the game.\n")
        elif third_choice.lower() == "jump":
            print("Your try to reach the ball in a jump, but it was without success, you loss your last chance and lose the game!\n ")
        else:
            print("You don't chose the right choice. This make your opponent wins the game. ")
    
    elif second_choice.lower() == "push":
        print("You push your opponent and he loss the balance loosing ball, the ball slede in your hand and your guide it close to you, but you blink your eyes and your opponent was there with the both hands in the ball, when your were loosing the balence. ")
    else:
        print("Youy opponent take the and run to far of you and you don't can get another opportunity to take the ball, in this way you loss the game. ")
elif first_choice.lower() == "wait":
    print("Your opponent ran until the ball, he picked up it and he took the ball to the corner of the playground. He put the ball in the floor and turn to you as a guard, kepping the ball close him.\n  ")
    second_choice = input("You can see some obstacles in your front until the ball in the corner, but you need to make a choice because the time is going out. You can pass through the OBSTACULES or turn around the RIGHT. \n\n")

    if second_choice.lower() == "obstacules":
        print("You pass through the obstacules as fast as you can, you learn a little how the opponent move hiself, and see that he limps with the left leg")
        third_choice = input("Now you can use your STRENGTH or AGILITY to take off the opponent's ball. ")
        if third_choice.lower() == "agility":
            print("You run in the opponent's direction, he was prepered to push you but you threatened go to your right, and turn to the left so faster that your opponent can't come back in time because his limps. You take the ball and win the game. ")
        elif third_choice.lower() == "strength":
            print("You use your strength against your opponent, but you don't expeted that he was so strong, he can hold you on far away the ball, the time was over when he push you and take the ball, he hold the ball until the time is over, and he wins the game. ")
        else:
            print("You try to take the ball sometimes but your opponent doesn't give you a chance to get close the ball. He took the ball before the time is over won the game.")
    elif second_choice.lower() == "right":
        print("You go through the right side avoiding the obstacules, but your give a lot of space to your opponent, so he goes out of the right corner with the ball and go to the left corner, and put the ball in the floor again, but in your percept he sprained his right foot. \n ")
        third_choice = input("The opponent decided to stay there, and you was approaching him, When you was passing close the two ideas, the first one was RUN into him and use all your speed and take the ball over him as fast as you can and run away or get close the ball and try to KICK it far from him. \n ")

        if third_choice.lower() == "run":
            print("You run, and use all your energi to win this game, you take the ball of you opponent and you close the eyes and hold the ball all the necessary time. When you open your eyes, you see your mother behind your bed with flowers, and explain that you were run over.")
        elif third_choice.lower() == "kick":
            print("You kick the ball too far away that neither you nor your opponent can achieve on time and touch the ball and the both are desqualifiqueted.")
        else:
            print("You run, and use all your energi to win this game, you take the ball of you opponent and you hold the ball all the necessary time in the end of match and you win.")
    else:
        print("When you are thinking in something to win the game, your life pass in your eyes, you don't remember anything, but you see a dear relative that pass away. You feel a great peace and now you understand that you pass away. It's a really game over to you. R.I.P.")

else:
    print("You felt anxiety and can make a move, you felt shortness of breath, and the medical time was help you. This match was canceled and you can try another time.")