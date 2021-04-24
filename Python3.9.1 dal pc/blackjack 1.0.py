import random
cash = 1000
deck = "Ace Ace Ace Ace Two Two Two Two Three Three Three Three Four Four Four Four Five Five Five Five Six Six Six Six Seven Seven Seven Seven Eight Eight Eight Eight Nine Nine Nine Nine Ten Ten Ten Ten Jack Jack Jack Jack Queen Queen Queen Queen King King King King ".split()
def Blackjack():
    cash = input("How many $ do you have?  ")
    bet = input("How many $ do you bet?  ")
    first_card = int(random.randint(1,13))
    if first_card == 1:
        value_first_card = 11
    if first_card > 1:
        value_first_card = first_card
    if first_card > 9:
        value_first_card = 10
    if first_card == 1:
        first_card = "Ace"
    if first_card != "Ace": 
        first_card = (first_card-1)*4+1
        first_card = deck[first_card]
    second_card = int(random.randint(1,13))
    if second_card == 1:
        value_second_card = 11
    if second_card > 1:
        value_second_card = second_card
    if second_card > 9:
        value_second_card = 10
    if second_card == 1:
        second_card = "Ace"
    if second_card != "Ace":
        second_card = (second_card-1)*4+1
        second_card = deck[second_card]
    first_card_dealer = int(random.randint(1,13))
    if first_card_dealer == 1:
        value_first_card_dealer = 11
    if first_card_dealer > 1:
        value_first_card_dealer = first_card_dealer
    if first_card_dealer > 9:
        value_first_card_dealer = 10
    if first_card_dealer == 1:
        first_card_dealer = "Ace"
    if first_card_dealer != "Ace":
        first_card_dealer = (first_card_dealer-1)*4+1
        first_card_dealer = deck[first_card_dealer]
    covered_card_dealer = round(random.randint(1,13))
    if covered_card_dealer == 1:
        value_covered_card_dealer = 11
    if covered_card_dealer > 1:
        value_covered_card_dealer = first_card
    if covered_card_dealer > 9:
        value_covered_card_dealer = 10
    if covered_card_dealer == 1:
        covered_card_dealer = "Ace"
    if covered_card_dealer != "Ace":
        covered_card_dealer = (covered_card_dealer-1)*4+1
        covered_card_dealer = deck[covered_card_dealer]
    if covered_card_dealer == "Jack" and first_card_dealer == "Ace" or covered_card_dealer == "Ace" and first_card_dealer == "Jack":
        print(first_card + " - " + second_card + " V.S. " + first_card_dealer + " - " + covered_card_dealer + ", BLACKJACK!")
        lose = round(bet*1.5)
        cash = int(cash-lose)
        print("You lose " + lose + "$")
    if second_card == "Jack" and first_card == "Ace" or second_card == "Ace" and first_card == "Jack":
        print(first_card + " - " + second_card + " V.S. " + first_card_dealer + " - " + covered_card_dealer + ", BLACKJACK!")
        gain = round(bet*1.5)
        cash = round(cash+gain)
        print("You gained " + gain + "$")
    print(first_card + " - " + second_card + " V.S. " + first_card_dealer + " - �")
    value_player = (value_first_card) + (value_second_card)
    print(value_player)
    print("V.S.")
    print(value_first_card_dealer)
    print(" ")
    for i in range(1):
        move = input("write DOUBLE DOWN, HIT, or STAND ----> ")
        if move == "HIT" or "Hit" or "hit":
            new_card = int(random.randint(1,13))
            if new_card == 1:
                value_new_card = 11
            if new_card > 1:
                value_new_card = new_card
            if new_card > 9:
                value_new_card = 10
            if new_card == 1:
                new_card = "Ace"
            if new_card != "Ace":
                new_card = (new_card-1)*4+1
                new_card = deck[new_card]
            new_value = value_player+value_new_card
            if new_value > 21:
                print(new_value)
                print("Your points went over 21, you lose " + bet + "$")
                cash = cash-bet
        if move == "STAND" or "Stand" or "stand":
            print(first_card + " - " + second_card + " - " + new_card + " V.S. " + first_card_dealer + " - � " + "- �")
            value_dealer = int(value_first_card_dealer + value_covered_card_dealer)
            print(value_player)
            print("V.S.")
            print(value_dealer)
            if value_player < value_dealer:
                cash = cash+bet
                print("The dealer has more points, you lose your bet.")
            if value_player == value_dealer:
                print("Push, money back.")
            if value_player > value_dealer:
                cash = cash+bet
                print("The player wins.")
        if move == "DOUBLE DOWN" or "Double Down" or "Double down" or "double down" or "DD" or "Dd" or "dd":
            new_card = int(random.randint(1,13))
            if new_card == 1:
                value_new_card = 11
            if new_card > 1:
                value_new_card = new_card
            if new_card > 9:
                value_new_card = 10
            if new_card == 1:
                new_card = "Ace"
            if new_card != "Ace":
                new_card = (new_card-1)*4+1
                new_card = deck[new_card]
            new_value = value_player+value_new_card
            if new_value > 21:
                print(new_value)
                bet = int(bet+bet)
                print("Your points went over 21, you lose your bet")
                cash = cash-bet
