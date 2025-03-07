from ascii_art import logo
import os

def clear_screen():
                if os.name == 'nt':
                    os.system('cls')

print(logo)

def biggest_bid_winner(bidding_dictionary):

    winner = ""
    biggest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > biggest_bid:
            biggest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} with the biggest bid of ${biggest_bid}")    

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("enter your name here: ")
    bid = int(input("enter your bid value here: $"))
    bids[name] = bid
    
    restart = input("Are there any other bidders (yes/no): ").lower()
    if restart == "no":
        clear_screen()
        continue_bidding = False
        biggest_bid_winner(bids)
    elif restart == "yes":
        clear_screen()