cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

def game_over():
    if user_score > 21 and i in user_cards != 11:
        print("You went over 21. Computer wins.")
    if computer_score > 21 and i in computer_cards == 11:
        print("Computer went over 21. User wins.")


def deal_card():
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

user_score = 0
computer_score = 0

def calculate_score():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if computer_score == 21:
        return 0
        print("Computer has Blackjack and wins.")
    if user_score == 21 and computer_score != 21:
        return 0
        print("User has Blackjack and wins.")
    if user_score or computer_score > 21:
        for i in user_cards:
            if i == 11:
                user_cards.remove(11)
                user_cards.append(1)
                user_score = sum(user_cards)
            else:
                game_over()
        for i in computer_cards:
            if i == 11:
                computer_cards.remove(11)
                computer_cards.append(1)
                computer_score = sum(computer_cards)
            else:
                game_over()





calculate_score()


def show_card():
    print(f"The computer has {str(computer_cards[0])} card.")
    print(f"The user has {str(user_cards[0:])} cards.")
    if user_score or computer_score == 21:
        if user_score == 21:
            compare()
            print("You win.")
        if computer_score == 21:
            compare()
            print("Computer wins.")




show_card()

def draw_card():
    if user_score or computer_score == 21:
        if user_score == 21:
            compare()
            print("You win.")
        if computer_score == 21:
            compare()
            print("Computer wins.")
    else:
        draw_card = input("Do you want to draw another card? Type Y or N. \n")
        if draw_card.upper() == "Y":
            user_cards.append(deal_card())
        if draw_card.upper() == "N":
            if computer_score < 17:
                computer_cards.append(deal_card())

draw_card()

def compare():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"User has {user_score}, computer has {computer_score}.")
    if user_score == 0:
        print("User wins.")
    if computer_score == 0:
        print("Computer wins.")
    if user_score > 21:
        print("User loses. Game over.")
    if computer_score > 21:
        print("Computer loses. Game over.")
    if user_score > computer_score and user_score <= 21:
        print("User has the highest score and wins")
    if computer_score > user_score and computer_score <= 21:
        print("Computer has the highest score and wins.")
    if user_score == computer_score:
        print("It's a draw.")

compare()

def run_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards.clear()
    computer_cards.clear()
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_score = 0
    user_score = 0
    calculate_score()
    show_card()
    draw_card()
    compare()
    restart_game()

def restart_game():
    restart_game = input("Do you want to restart the game? Type Y or N. \n")
    if restart_game.upper() == "Y":
        run_game()

    if restart_game.upper() == "N":
        print("Have a nice day.")

restart_game()
