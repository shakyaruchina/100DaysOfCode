
bids={}
bidding_finished = False

#bidding record = dictionary: records all the inputs
def highest_bidder(bidding_record):
    #{Name: Value, Name:Value}
    highest_bid = 0
    winner= ""
    for bidder in bidding_record:
        #Dictionary to get value biddingrecord[bidder]
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    userName = input("What is your name? ")
    userBidPrice = int(input("What is your bid price? $"))
    #dictionary #dictionary bids
    #new entry [key] = [value]
    bids[userName] = userBidPrice
    anyNewUser = input("Is there any new users? Yes or No? ")
    if anyNewUser == "No":
        bidding_finished = True
        highest_bidder(bids)
    