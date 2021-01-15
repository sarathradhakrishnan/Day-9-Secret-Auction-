from art import logo
import os
print(logo)
auction ={}
ans ="true"
def final_bid(auction_bid):
    highest_bid = '0'
    winner =""
    for bid in auction_bid:
        bid_amount =auction_bid[bid]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner =bid
    print(f"The winner of todays bidding is {winner} with a bid of ${highest_bid}") 


while ans=="true":
    name =input("Please enter your name\n")
    bid_amt =input("Please enter your bidding amount $")
    auction[name]=bid_amt
    final =input("Are there any other bidders?,type yes or no\n")
    if final =="yes":
        os.system('cls')
    else:
        final_bid(auction)
        ans ="false"