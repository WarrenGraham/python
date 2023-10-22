import random

def print_card_status(crupier_second_card='X', crupier_third_card=False):
    if crupier_third_card == False:
        print(f'Your cards are {player_cards}, dealers cards are [{dealer_cards[0]}, {crupier_second_card}]. Your points are summing to {sum(player_cards)}') 
    else:
        print(f'Your cards are {player_cards}, dealers cards are {dealer_cards} They are summing to {sum(dealer_cards)}. Your points are summing to {sum(player_cards)}') 

def ace_grabber():
    if player_cards[-1] == 11 and sum(player_cards) > 21:
        player_cards[-1] = 1

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = random.choices(cards, k=2)
player_cards = random.choices(cards, k=2)

print_card_status()
player_choise = input('Do you want to hit or stand. Press "hit" or "stand"\n').lower()


while player_choise == 'hit' and sum(player_cards) <= 21:
    player_cards.append(random.choice(cards))
    ace_grabber()
    if sum(player_cards) <= 21:
        print_card_status()
        player_choise = input('Do you want to hit or stand. Press "hit" or "stand"\n').lower()
    else:
        print_card_status()
        print('YOU EXCEEDED 21, YOU LOSE!!!')

if player_choise == 'stand' and sum(player_cards) <= 21:
    print_card_status(crupier_second_card=dealer_cards[1])
    if sum(dealer_cards) < 17:
        print('Crupier have less than 17 points, thats why needs to hit one more card:')
        dealer_cards.append(random.choice(cards))
        ace_grabber()
        print_card_status(crupier_third_card=True)

if sum(player_cards) <= 21:
    if sum(dealer_cards) > 21:
        print('Crupier exceeded 21 points. YOU WIN!!!')
    elif sum(dealer_cards) > sum(player_cards):
        print('Crupier has more points than you. YOU LOSE!!!')
    elif sum(dealer_cards) < sum(player_cards):
        print('You have more points than crupier. YOU WIN!!!')
    elif sum(dealer_cards) == sum(player_cards):
        print('There is a draw')


