import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
hand=[]
computer=[]
logo="""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                      """
score1=0#this holds the score for the player
score2=0 #this is adding the score for the computer
print(logo)

for _ in range(2):
    selection1=cards.index(random.choice(cards))#this is picking a random number from the cards list by using random and also the index as well
    #print(selection1) #This is here so I can see the list postion that gets selected

    selection2=cards.index(random.choice(cards))#same as selection one but this selection is used for the computer
    #print(selection2)

    score1=score1+cards[selection1]#this is adding the score for the player
    #print(score1) 

    score2=score2+cards[selection2]#this is adding the score for the computer
    #print(score2)#printing the score for the computer

    hand.append(cards[selection1])#this is adding the number from the cards list to the player list
    computer.append(cards[selection2])#this is adding the number from the cards to the computers list

def nn(pick,score1,score2,selection1,selection2):
        
        if pick.lower() == 'y':
            selection1=cards.index(random.choice(cards))
            if cards[selection1] == 11:
                if score1+cards[selection1]> 21:
                    ace=int(input("You pulled an ace type '1' for 1 or type '11' for 11: "))
                    score1=score1+ace
                    hand.append(ace)
            else:
                score1=score1+cards[selection1]
                hand.append(cards[selection1])      

            if score1<21:
                print(f"Your hand: {hand} score: {score1}")
                print(f"Computers score: {computer[0]}")
                pick=input("Type 'y' to get another card, type 'n' to pass: ")
                nn(pick,score1,score2,selection1,selection2)

            elif score1 == 21:
                print(f"You got {score1}")
                print("You win!🏆")
            elif score1>21:
                print(f"Your final hand {hand}, final score: {score1}")
                print(f"Dealers hand is {computer}, final score: {score2}")
                print("You went over. You lose😭11")

        if pick.lower() == "n":
            if score2<17:
                selection2=cards.index(random.choice(cards))
                score2=score2+cards[selection2]
                computer.append(cards[selection2])
                if score2==21:
                    print(f"Your final hand: {hand} final score: {score1}")
                    print(f"Computers final hand {computer}, final score: {score2}")
                    print("You lose😭12")
                elif score2<score1:
                    print(f"Your final hand: {hand} final score: {score1}")
                    print(f"Computers final hand {computer}, final score: {score2}")
                    print("You win!🏆11")
                elif score2>score1:
                    if score2 > 21:
                        print(f"Your final hand: {hand} final score: {score1}")
                        print(f"Computers final hand {computer}, final score: {score2}")
                        print("You win🏆12")
                    elif score2 < 21:
                        print(f"Your final hand: {hand} final score: {score1}")
                        print(f"Computers final hand {computer}, final score: {score2}")
                        print("You lose😭13")

            elif score2>=17:
                    if score2 == 21:
                        print(f"You had {hand} and your score: {score1}")
                        print(f"The dealer had {computer} and the score: {score2}")
                        print("You lose😭1")
                    elif score2>score1:
                        if score2<21:
                            print(f"Your final hand: {hand} final score: {score1}")
                            print(f"Computers final hand {computer}, final score: {score2}")
                            print("You lose😭2")
                        elif score2>21:
                            print(f"Tester:{computer}")
                            print("You win🏆1")
                    elif score2 == score1:
                        print(f"You had {hand} and your score: {score1}")
                        print(f"The dealer had {computer} and the score: {score2}")
                        print("This is a draw")
                    elif score2<score1:
                        if score1<21:
                            print("You win🏆1")
                        else:
                            print("You lose😭")
         

print(f"Your cards: {hand}, current score: {score1}")
print(f"Computer's first card: {computer[0]} ")
print(f"Tester:{computer}")
if score1 == 21:
    print("You win")
else:
    pick=input("Type 'y' to get another card, type 'n' to pass: ")
    nn(pick,score1,score2,selection1,selection2)




