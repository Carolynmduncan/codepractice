from replit import clear
silent_auction = {}

import math
import art
print(art.logo)

def add_bids():
  clear()
  print(art.logo)
  name = input("What is your name?\n")
  bid = input("What is your bidding price?\n $")
  silent_auction[name] = int(bid)
  
  more_bids = input("Are there any other people who want to bid? Type Y for yes or N for no.\n")
  if more_bids.upper() == "Y":
    add_bids()
  else:
    for value in silent_auction.values():
      all_bids = silent_auction.values()
      highest_bid = max(all_bids)
      highest_bidder = max(silent_auction, key=silent_auction.get) 
    print(f"The winner is {highest_bidder} with ${highest_bid}!")
add_bids()
