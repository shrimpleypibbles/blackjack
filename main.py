import random
from replit import clear
from art import logo


def deal_card():
    """returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """takes list of cards and returns the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    else:
        return sum(cards)


def compare(user_score, computer_score):
    """compares the user_score and the computer_score"""
    if user_score == computer_score:
        return "This game ends in a draw. Schade. "
        game_over = True
    elif user_score > 21:
        return "BUST. You went over, you lose. "
        game_over = True
    elif computer_score > 21:
        return "The computer went BUST. You win! "
        game_over = True
    else:
        if user_score == 0 or user_score > computer_score:
            return "You won! "
        elif computer_score == 0 or computer_score > user_score:
            return "You lost. "


#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            print(compare(user_score, computer_score))
            game_over = True
        else:
            if input("Type 'y' to be dealt another card, type 'n' to pass: "
                     ) == "y":
                user_cards.append(deal_card())
            else:
                user_score = calculate_score(user_cards)
                computer_score = calculate_score(computer_cards)
                print(
                    f"Your final cards: {user_cards}, your current score: {user_score}"
                )
                print(
                    f"Computer's final cards:' {computer_cards}, computer's score: {computer_score}"
                )
                print(compare(user_score, computer_score))
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py


while input("Would you like to play a game of Blackjack? Enter 'y' or 'n': "
            ) == "y":
    clear()
    play_blackjack()
else:
    clear()