deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    shuffled_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]

    for card_index in range(0, len(left_part)):
        shuffled_deck.append(left_part[card_index])
        shuffled_deck.append(right_part[card_index])
        card_index += 1
    deck_of_cards = shuffled_deck
print(deck_of_cards)



