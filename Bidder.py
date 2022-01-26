from replit import clear
from Bid_art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("Enter your name:")
    price = int(input("Enter the bid price in PKR: RS"))
    #price1 = (f"{price}RS.") 
    #print(name)
    #print(price1)
    bids[name] = price
    should_continue = input("Are there any other bidders: Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        find_highest(bids)
    elif  should_continue == "yes": 
        clear()
    


    #It is from replit,so "clear()" will not work.