from random import *
from time import *


cards = ["coins🪙", "clubs🪵", "swords⚔️", "cups🏆"]
value = ["Ace(1)", "Two(2)", "Three(3)", "Four(4)", "Five(5)", "Six(6)", "Seven(7)", "Knave(8)", "Knight(9)", "King(10)"]
a = ""
dealer = 0
player = 0
credits = 200

def draw_card():
    number_drawn = number_of_cards.pop()           #draws a card from the deck
    card_suit = number_drawn // 10           #gets the integer part of the divison to determine the suit       
    card_value = number_drawn % 10           #determinates the value of the card
    real_value = card_value + 1            #gives the real value of the card(lists starts with 0)
    
    if dealer_turn == False:              #checks if it's the turn of the player or the dealer
        print("Your card:", value[card_value], "of", cards[card_suit])       #print the name of the card
    else:
        print("Dealer card:", value[card_value], "of", cards[card_suit])      #print the name of the card

    return real_value, number_drawn

def manage_jolly(isJolly, totPoints):
    if isJolly == 7 and totPoints < 7.5:                    #checks if you drawn the jolly and not busted
        if totPoints % 1 == 0 and totPoints != 7:           #checks if your point is an integer and not 7
            jolly_total_points = 7                          #gives your point a 7 because you've drawn the jolly
        elif totPoints % 1 != 0 or totPoints == 7:          #checks if your points haves an half
            jolly_total_points = 7.5                        #gives you the maximum of points because of the jolly
        sleep(0.5)

    if isJolly == 0 or totPoints > 7.5:                     #checks if the jolly was not drawn and gives a print of total points
        if dealer_turn == False:
            print("You have", totPoints)
        else:
            print("Dealer has", totPoints)
        return totPoints
    elif isJolly == 7 and totPoints <= 7.5:                 #checks if the jolly wasa drawn and gives the total points with the jolly
        if dealer_turn == False:
            print("You have", jolly_total_points)
        else:
            print("Dealer has", jolly_total_points)
        return jolly_total_points
    
def manage_points_card(isJolly, cardPoints, totPoints):
    if cardPoints > 7 and isJolly != 9:                     #checks if the card is greater then 7 and not the jolly
        points = 0.5                                        #and then gives a value of 0.5 to the card
        totPoints += points                                 
        jolly_value = 0
    elif isJolly == 9:                                      #checks if it is the jolly
        jolly_value = 7                                     #and gives a value of 7
        sleep(0.5)
        if dealer_turn == False:
            print("You drawn the jolly")
        else:
            print("The dealer drawn the jolly")
    else:
        points = cardPoints                                 #else if it is a card smaller or equal to 7 it gives its nominal value
        totPoints += points
        jolly_value = 0

    return jolly_value, totPoints

def check_win(dealerPoints, playerPoints, playerCredits, dealerStats, playerStats, playerBid):
    if dealerPoints >= playerPoints and dealerPoints <= 7.5:
        print("The dealer won")
        dealerStats += 1
        playerCredits -= playerBid
        print("Dealer:", dealerStats, "You:", playerStats, "Now you have", playerCredits, "credits")
            
    elif dealerPoints < playerPoints and dealerPoints <= 7.5:
        print("You won!")
        playerStats += 1
        playerCredits += playerBid
        print("Dealer:", dealerStats, "You:", playerStats, "Now you have", playerCredits, "credits")
            
    elif dealerPoints > 7.5:
        print("You won!")
        playerStats += 1
        playerCredits += playerBid
        print("Dealer:", dealerStats, "You:", playerStats, "Now you have", playerCredits, "credits")

    return dealerPoints, playerPoints, playerCredits, dealerStats, playerStats



print("Welcome to seven and an half!")
while credits > 0:

    input("Press enter to start ")
    number_of_cards = list(range(40))       #creates a deck of 40 cards
    shuffle(number_of_cards)                #shuffles the deck
    jolly_value = 0
    points = 0
    total_points = 0
    bid = 1000000000000000

    sleep(0.5)

    while bid > credits:
        print("You have", credits, "credits")                               #it prints your total credits
        sleep(0.5)
        bid = int(input("How much do you want to bid? "))               #ask how much credits you want to bid
        if bid > credits:                                               #if the bid is greater than the total credits 
            print("You can't bid more credits than the ones you have")     
    
    
    
        
    print("Shuffle the deck...")
    sleep(2)

    #PLAYER TURN
    dealer_turn = False
    CardValue, CardID = draw_card()
    jolly_value, total_points = manage_points_card(CardID, CardValue, total_points)
    total_points = manage_jolly(jolly_value, total_points)
        
    sleep(0.5)

    keep_or_card = input("Keep or card? (keep/card) ")
    while keep_or_card == "card":
       
        CardValue, CardID = draw_card()
        
        jolly_value, total_points = manage_points_card(CardID, CardValue, total_points)
        
        total_points = manage_jolly(jolly_value, total_points)
    
        sleep(0.5)
        
        if total_points > 7.5 :                                         #if the total points are > 7.5
            print("You busted")                                         #the program prints that you busted
            print("The dealer won")
            dealer = dealer + 1
            credits = credits - bid
            print("Dealer:", dealer, "You:", player, "Now you have", credits, "credits")                                     #and remove the lost credits
            break
        elif total_points == 7.5:
            keep_or_card = "keep"
        if total_points < 7.5:
            keep_or_card = input("Keep or card? (keep/card) ")
    if total_points <= 7.5:
        print("You keep with", total_points)
        sleep(0.5)
    
    #DEALER TURN
        dealer_turn = True
        total_dealer_points = 0
        CardValue, CardID = draw_card()
        jolly_value, total_dealer_points = manage_points_card(CardID, CardValue, total_dealer_points)
        total_dealer_points = manage_jolly(jolly_value, total_dealer_points)

        if total_dealer_points >= total_points:
            keep_or_card = "keep"
        else:
            keep_or_card = "card"
         
        while keep_or_card == "card":
            sleep(1)
            print("The dealer draws another card")
            sleep(1)
            
            CardValue, CardID = draw_card()
            jolly_value, total_dealer_points = manage_points_card(CardID, CardValue, total_dealer_points)
            total_dealer_points = manage_jolly(jolly_value, total_dealer_points)

            sleep(1)

            if total_dealer_points >= total_points:
                keep_or_card = "keep"
            else:
                keep_or_card = "card"
            if total_dealer_points > 7.5:
                sleep(1)
                print("The dealer busted")
                break
            
        sleep(1)
            

        total_dealer_points, total_points, credits, dealer, player = check_win(total_dealer_points, total_points, credits, dealer, player, bid)
        
        sleep(1)

print("You finished all your credits")

