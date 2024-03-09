# Auction Program
# ####### Data Structures
# Data Structure 1: {"Ahmad": "$1000", "Angela": "$500", "Salman": "$900"}
# Data Structure 2: [ { "name": "Ahmad", "bid": "$1000" } ]
# ####### Algorithm
# 1- Get user name : Ahmad, Get user bid: $1000,
# 2- Check if new user = TRUE

is_new_bidder = True
bidders = {}
winner = ""
def auction(name, bid):
    bidders[name] = bid
def winner_of_auction():
    high_bid = 0
    for bidder in bidders:
        bid = bidders[bidder]
        if bid > high_bid:
            high_bid = bid
            winner = bidder
    print(f"Winner is {winner} with high bid of {high_bid}")
    
while is_new_bidder:
    get_name = input("What is your name?: ")
    get_bid = int(input("What is your bid?: $"))
    auction(get_name, get_bid)
    check_new_user = input("If new bidder type 'yes', else 'no': ")
    if check_new_user == "no":
        is_new_bidder = False
        winner_of_auction()
        
            
            
    