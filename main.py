from random import choice
import os


total_score = 0

initial_balance = 1200
print(f"your initial-bank balance {initial_balance}")
Deal = int(input("Select dealing amount : \n$50\n$60\n$70\n$100\n"))

if Deal == 50 or Deal == 60 or Deal == 70 or Deal == 100:
    initial_balance -= Deal
    os.system("clear")
    print(f"your balance {initial_balance}")

else:
    print("Select Valid amount ! ")

blackjack_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
player = []
computer = []
true_or_false = True
i = 0
while i < 2:
    player.append(choice(blackjack_cards))
    computer.append(choice(blackjack_cards))
    i += 1
print(f"your cards {player},current score : {sum(player)}")
# print(computer)
while true_or_false:
    select_option = input("Type 'y' to get another card, type 'n' to pass : ")

    if select_option == "n" or select_option == "N":
        true_or_false = False
        os.system("clear")
        print(f"your final hand {player}, your score : {sum(player)}")
        print(f"computers final hand {computer},computer score {sum(computer)}")
        if sum(player) > sum(computer) and sum(player) < 21:
            print("you win")
        elif sum(player) == sum(computer):
            print("draw")
        else:
            print("computer win, you loose")
            os.system("clear")

    elif select_option == "Y" or select_option == "y":
        player.append(choice(blackjack_cards))

        print(f"your cards {player},current score : {sum(player)}")
        print(f"computer first card :{computer[0]}")
        if sum(player) >= 21:
            print(f"your final hand {player}, your score : {sum(player)}")
            print(f"computers final hand {computer},computer score {sum(computer)}")
            if sum(player) > sum(computer) and sum(player) < 21:
                print("you win")
            elif sum(player) == sum(computer):
                print("draw")
            else:
                print("computer win, you loose")
                break

    else:
        print("Select valid option ")
