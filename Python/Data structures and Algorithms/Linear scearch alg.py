# Problem:

# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# Solution:
    
cards = [13, 11, 10, 7, 4, 3, 1, 0]
quarry = 7
# expected output: 3

def locate_card(cards, quarry):
    position = 0
    
    while True:
        if cards[position] == quarry:
            return position
        position += 1
        
        if position == len(cards):
            return -1

card_location = locate_card(cards, quarry)
print(card_location)