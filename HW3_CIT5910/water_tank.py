# TODO: Students, fill out statement of work header
# Student Name in Canvas:Souley Diallo
# Penn ID:
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: None

# import statements
from random import shuffle

def get_user_input(question):
    
    """Prompt the user with the given question and process the input. Return the post-processed user input.
        - Remove leading and trailing whitespaces.
        - If the length of the user input after removing leading and trailing whitespaces is 0, reprompt.
        - If the input is a number, cast and return an integer type.
        - If the input is a power card, return the power card as an uppercase string.
        - If the input is any other string, return the string as a lowercase string.
    """
    start = True

    power_card = setup_power_cards()

    while start:
        user = input(question).strip()
        if user:
            start = False
        else:
            start = True
        try:
            if user.isdigit():
                return int(user)
            elif user == power_card:
                return power_card.upper()
            else:
                return user.lower()
        except:
            return "Invalid entry"

    return user
                        

def setup_water_cards():

    """Create a shuffled list of water cards with the following values and quantities.
    values: [1, 5, 10], quantities: [30, 15, 8]
    Hint: Use the shuffle function from the random module. 
    Return the water cards as a list of integers"""

    values = [1,5,10]
    quantities = [30, 15, 8]
    water_cards = []

    for value, quantity in zip(values, quantities):
        water_cards.append(value * quantity)
    
    shuffle(water_cards)

    return water_cards


def setup_power_cards():
    """Create a shuffled list of power cards with the following values and quantities:
    values: [SOH, DOT, DMT]
    quantities: [10, 2, 3]
    Decription: [Steal half opponent's tank value. If the opponent's tank value is an odd integer, it will truncate the decimal value (Example: ½ of 5 is 2) Hint: You may use the cast to int, Drain opponent's tank, Double my tank's value.]
    
    Hint: Use the shuffle function from the random module. 
    Return the power cards as a list of strings.
    """

    values = ['SOH', 'DOT', 'DMT']
    quantities = [10, 2, 3]
    power_cards = []
    for value, quantity in zip(values,quantities):
        power_cards.append(value * quantity)
    
    shuffle(power_cards)

    return power_cards


def setup_cards():
    """Set up both the water card and power card piles as described in the setup_water_cards and setup_power_cards functions.
    Return a 2-tuple containing the water cards pile and the power cards pile, respectively.(Each pile should be represented by a list.)
    """

    water_card = setup_water_cards()
    power_card = setup_power_cards()

    return (water_card, power_card)


def get_card_from_pile(pile, index):
    """Removes the entry at the specified index of the given pile (water or power) and modifies the pile by reference. 
    This function returns the entry at the specified index. HINT: Use the pop function
    """
    return pile.pop(index)



def arrange_cards(cards_list):
    """Arrange the players cards such that: 
        The first three indices are water cards, sorted in ascending order. 
        The last two indices are power cards, sorted in alphabetical order.
    This function doesn't return anything.
    """
    water_card = [card for card in cards_list if isinstance(card, int)]
    power_card = [card for card in cards_list if isinstance(card, str)]
    water_card.sort()
    power_card.sort()

    cards_list[:] = water_card[:3] + power_card[:2]

def deal_cards(water_cards_pile, power_cards_pile):
    """Deals cards to player 1 and player 2. Each player would get 3 water cards and 2 power cards. Then, call the arrange_cards function to arrange the cards.
    When dealing, alternately take off a card from the first entry in the pile.
    
    Return a 2-tuple containing the player 1's hand and player 2's hand, respectively. (Each hand should be represented by a list.)
    """

    player_1 = []
    player_2 = []

    for _ in range(3):
        player_1.append(water_cards_pile.pop(0))
    
    for _ in range(2):
        player_2.append(power_cards_pile.pop(0))
    
    player_1_cards = arrange_cards(player_1)
    player_2_cards = arrange_cards(player_2)

    return (player_1_cards, player_2_cards)



def apply_overflow(tank_level):
    """If necessary, apply the overflow rule discussed in the “About the Assignment” section of this assignment.
        
        remaining water = maximum fill value - overflow
    
    Return the tank level. If no overflow occurred, this is just the starting tank level.
    """
    maximum_fill_value = 80
    overflow = 10
    if tank_level > maximum_fill_value:
        remaining_water = maximum_fill_value - overflow
        return remaining_water
    else:
        return tank_level


def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    """Get that card from the player's hand, and update the tank level based on the card that was used. This does no include drawing a replacement card, so after using the card, the player_cards size will only be 4 cards. 
    
    Apply overflow if necessary.

    Return a 2-tuple containing the player's tank and the opponent's tank, respectively.
    """
    card_value = player_cards.pop(card_to_use)
    player_tank += card_value
    opponent_tank += card_value

    if player_tank > 80:
        apply_overflow(player_tank)
    if opponent_tank > 80:
        apply_overflow(opponent_tank)
    
    return (player_tank, opponent_tank)


def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    """Discard the given card from the player's hand and return it to the bottom of the
    appropriate pile. (Water cards should go in the water card pile and power cards should go in the power card pile.) The bottom of the pile is the last index in the list.
    
    Same as use_card(), this function does not include drawing a replacement card, so after calling this function, the player_cards size will only be 4 cards.
    
    This function does not return anything.
    """
    card_value = player_cards.pop(card_to_discard)
    if water_cards_pile:
        water_cards_pile[:-1] = card_value
    if power_cards_pile:
        power_cards_pile[:-1] = card_value


def filled_tank(tank):
    """Determine if the tank level is between the maximum and minimum fill values (inclusive).
    
    Return a boolean representing whether the tank is filled.
    This will be True if the tank is filled.
    """
    maximum_value = 80
    minimum_value = 75
    if minimum_value <= tank <= maximum_value:
        return True
    return False


def check_pile(pile, pile_type):
    """Checks if the given pile is empty. If so, call the pile's setup function to replenish the pile. 
    pile_type is a string to determine what type of pile you are checking (“water” or “power”)
    This function does not return anything.
    """
    if len(pile) == 0:
        if pile_type == 'water':
            pile.extend(setup_water_cards())
        elif pile_type == 'power':
            pile.extend(setup_power_cards())
    

def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    - Show the human player's water level and then the computer player's water level.
    - Show the human player their hand and ask them if they want to use or discard a card. If the human player enters an invalid answer, reprompt until a valid answer is entered.
    - Carry out the human's turn based on the action they have chosen (based on user input). 
    Be sure to use the get_user_input function.
    - Print the card the human player uses or discards. If the human player enters a card to use or discard which is not in their hand, reprompt until a valid card is entered.
    - Remember to handle potential overflows.
    - Once the human has used or discarded a card, draw a new card of the same type they just used/discarded.
    - Make sure that the human's hand is still properly arranged after adding the new card.
    - Return a 2-tuple containing the human's tank level and the computer's tank level, respectively.
    """

    print('Human tank {}\n'.format(human_tank))
    print('Computer tank {}\n'.format(opponent_tank))
    print('Human player\'s hand {}\n'.format(human_cards))
    while True:
        card = get_user_input('Would you like to use or discard? ')
        if card in human_cards:
            print('Card played or discarded: ', card)
            human_cards.remove(card)
            if isinstance(card, int):
                human_tank += apply_overflow(card)
                new_card = get_card_from_pile(water_cards_pile, 0)
            else:
                new_card =get_card_from_pile(power_cards_pile, 0)
            human_cards.append(new_card)
            arrange_cards(human_cards)
            break
        else:
            print('Invalid entry, please choose a card from your hand.')

    return (human_tank, opponent_tank)



def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
      """This is the function where you can write the computer's strategy. 
      - You are supposed to be somewhat creative here, but make sure your code is deterministic (not random).
      - The computer's strategy should consider all of its cards when playing. For example, you should not have a strategy where the computer always plays the first water card or the first power card.
      - The computer should not “cheat.” They should not be able to see any cards from the human's hand, the water card pile or power card pile. When they draw a card, they should only see that card and no cards from the rest of the water or power card pile.
      - This function should carry out the computer's turn based on the action that the computer chooses.
      - Remember to handle potential overflows.
      - Print the card the computer player uses or discards.
      - Once the computer has used or discarded a card, give them a new card of the same type they just used/discarded.
      - Make sure that the computer's hand is still properly arranged after adding the new card.
      - Return a 2-tuple containing the computer's tank level and the human's tank level, respectively
      """




def main():
	"""The main function would be where you would structure the flow of your game, calling the functions defined above, as needed. As noted in the “User Interface” section of this assignment, remember to choose a random player to go first. For each turn, a player can use a card (then draw a new card) or discard a card (then draw a new card).
    """
    # TODO: Write your code as described in the instructions



if __name__ == '__main__':
    main()
