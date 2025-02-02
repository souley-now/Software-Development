# TODO: Students, fill out statement of work header
# Student Name in Canvas:Souley Diallo
# Penn ID:
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: None


# import statements
import random

def get_user_input(question):
    
    """Prompt the user with the given question and process the input. Return the post-processed user input.
        - Remove leading and trailing whitespaces.
        - If the length of the user input after removing leading and trailing whitespaces is 0, reprompt.
        - If the input is a number, cast and return an integer type.
        - If the input is a power card, return the power card as an uppercase string.
        - If the input is any other string, return the string as a lowercase string.
    """
    # Initialize power cards
    power_cards = setup_power_cards()

    # Create loop to continuously prompt the user until valid input is received
    while True:
        # Prompt the user and remove leading/trailing whitespaces
        user = input(question).strip()
        
        # Check if the input is empty
        if not user:
            print('Input can\'t be empty. Please try again.')
            continue
        
        # Check if the input is a number and return it as an integer
        if user.isdigit():
            return int(user)
        # Check if the input is a power card and return it as an uppercase string
        elif user.upper() in power_cards:
            return user.upper()
        # For any other string input, return it as a lowercase string
        else:
            return user.lower()
                        


def setup_water_cards():

    """Create a shuffled list of water cards with the following values and quantities.
    values: [1, 5, 10], quantities: [30, 15, 8]
    Hint: Use the shuffle function from the random module. 
    Return the water cards as a list of integers"""

    # Define the values and quantities of the water cards
    values = [1,5,10]
    quantities = [30, 15, 8]
    
    # Create the list of water cards
    water_cards = []
    for value, quantity in zip(values, quantities):
        water_cards.extend([value] * quantity)
    
    # Shuffle the water cards
    random.shuffle(water_cards)

    # Return the shuffled list of water cards
    return water_cards


def setup_power_cards():
    """Create a shuffled list of power cards with the following values and quantities:
    values: [SOH, DOT, DMT]
    quantities: [10, 2, 3]
    Decription: [Steal half opponent's tank value. If the opponent's tank value is an odd integer, it will truncate the decimal value (Example: ½ of 5 is 2) Hint: You may use the cast to int, Drain opponent's tank, Double my tank's value.]
    
    Hint: Use the shuffle function from the random module. 
    Return the power cards as a list of strings.
    """

    # Define the values and quantities of the power cards
    values = ['SOH', 'DOT', 'DMT']
    quantities = [10, 2, 3]
    
    # Create the list of power cards
    power_cards = []
    for value, quantity in zip(values, quantities):
        power_cards.extend([value] * quantity)
    
    # Shuffle the power cards
    random.shuffle(power_cards)

    # Return the shuffled list of power cards
    return power_cards

def setup_cards():
    """Set up both the water card and power card piles as described in the setup_water_cards and setup_power_cards functions.
    Return a 2-tuple containing the water cards pile and the power cards pile, respectively.(Each pile should be represented by a list.)
    """

    # Set up the water cards and power cards
    water_card = setup_water_cards()
    power_card = setup_power_cards()

    # Return a tuple containing water cards and power cards
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
    if not cards_list:
        return
        
    # Separate water cards (integer) and power card (strings)
    water_card = [card for card in cards_list if isinstance(card, int)]
    power_card = [card for card in cards_list if isinstance(card, str)]
    
    # Sort cards
    water_card.sort()
    power_card.sort()

    # Create a list of the hand, ensuring we have enough cards
    water_cards_to_use = water_card[:3] if len(water_card) >= 3 else water_card
    power_cards_to_use = power_card[:2] if len(power_card) >= 2 else power_card
    
    cards_list[:] = water_cards_to_use + power_cards_to_use


def deal_cards(water_cards_pile, power_cards_pile):
    """Deals cards to player 1 and player 2. Each player would get 3 water cards and 2 power cards. Then, call the arrange_cards function to arrange the cards.
    When dealing, alternately take off a card from the first entry in the pile.
    
    Return a 2-tuple containing the player 1's hand and player 2's hand, respectively. (Each hand should be represented by a list.)
    """

    player_1 = []
    player_2 = []

    # Deal 3 water cards to each player and reduce the water card pile
    for _ in range(3):
        player_1.append(get_card_from_pile(water_cards_pile, 0))
        player_2.append(get_card_from_pile(water_cards_pile, 0))

    # Deal 2 power cards to each player and reduce the power card pile
    for _ in range(2):
        player_1.append(get_card_from_pile(power_cards_pile, 0))
        player_2.append(get_card_from_pile(power_cards_pile, 0))

    # Arrange cards for both players
    arrange_cards(player_1)
    arrange_cards(player_2)

    return (player_1, player_2)



def apply_overflow(tank_level):
    """If necessary, apply the overflow rule discussed in the “About the Assignment” section of this assignment.
        
        remaining water = maximum fill value - overflow
    
    Return the tank level. If no overflow occurred, this is just the starting tank level.
    """
    maximum_fill_value = 80
    if tank_level > maximum_fill_value:
        overflow = tank_level - maximum_fill_value
        return maximum_fill_value - overflow
    return tank_level   



def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    """Get that card from the player's hand, and update the tank level based on the card that was used. This does not include drawing a replacement card, so after using the card, the player_cards size will only be 4 cards. 
    
    Apply overflow if necessary.

    Return a 2-tuple containing the player's tank and the opponent's tank, respectively.
    """
    card_value = player_cards.pop(card_to_use)
    
    if isinstance(card_value, int):
        player_tank += card_value
        if player_tank > 80:
            player_tank = apply_overflow(player_tank)
    else:
        if card_value == 'SOH':
            opponent_tank = int(opponent_tank / 2)
        elif card_value == 'DOT':
            opponent_tank = 0
        elif card_value == 'DMT':
            player_tank = apply_overflow(player_tank * 2)
    
    return (player_tank, opponent_tank)


def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    """Discard the given card from the player's hand and return it to the bottom of the
    appropriate pile. (Water cards should go in the water card pile and power cards should go in the power card pile.) The bottom of the pile is the last index in the list.
    
    Same as use_card(), this function does not include drawing a replacement card, so after calling this function, the player_cards size will only be 4 cards.
    
    This function does not return anything.
    """
    card_value = player_cards.pop(card_to_discard)

    if isinstance(card_value, int):
        water_cards_pile.append(card_value)
    else:
        power_cards_pile.append(card_value)

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
        if pile_type.lower() == 'water':
            pile.extend(setup_water_cards())
        elif pile_type.lower() == 'power':
            pile.extend(setup_power_cards())
        else:
            print("Invalid inputs, please enter 'water' or 'power'.")
    

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

    print("Human water tank level is {}. Opponents water tank level is {}. Human cards are {}".format(human_tank, opponent_tank, human_cards) )
    
    while True:
        action = get_user_input('Would you like to "use" or "discard" a card? ').lower()
        if action not in ["use", "discard"]:
            print('Invalid action. Please enter "use" or "discard".')
            continue
        
        card = get_user_input('Which card would you like to {}? '.format(action))
        if card in human_cards:
            print('Card {}ed: {}'.format(action, card))
            card_index = human_cards.index(card)
            if action == "use":
                human_tank, opponent_tank = use_card(human_tank, card_index, human_cards, opponent_tank)
                if human_tank > 80:
                    if isinstance(card, int):
                        potential_tank = apply_overflow(human_tank + card)
                        if filled_tank(potential_tank):
                            print('Congrats, you have won!')
                        break
                else:
                    if filled_tank(human_tank):
                        print("Congrats you have won!")
                        break
            else:
                discard_card(card_index, human_cards, water_cards_pile, power_cards_pile)
            
            if isinstance(card, int):
                new_card = get_card_from_pile(water_cards_pile, 0)
            else:
                new_card = get_card_from_pile(power_cards_pile, 0)
            
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

    best_card = None
    best_card_type = None

    # Iterate through the computer's cards to find the best card to play
    for card in computer_cards:
        if isinstance(card, int):  # Check if the card is a water card
            potential_tank = apply_overflow(computer_tank + card)
            if filled_tank(potential_tank):
                best_card = card
                best_card_type = 'water'
                break
            if best_card is None or (card > best_card and computer_tank + card <= 80):
                best_card = card
                best_card_type = 'water'
        else:  # Check if the card is a power card
            if best_card is None or (best_card_type == 'water' and card in ['SOH', 'DOT', 'DMT']):
                best_card = card
                best_card_type = 'power'

    if best_card is not None:
        if best_card.isdigit():
            if not filled_tank(computer_tank):
                # Remove the best card from the computer's hand
                computer_cards.remove(best_card)
                if best_card_type == 'water':
                    computer_tank += best_card
                    if computer_tank > 80:
                        # Apply overflow rules to the computer's tank
                        computer_tank = apply_overflow(computer_tank)
                    # Draw a new water card from the pile
                    new_card = get_card_from_pile(water_cards_pile, 0)
        else:
            if not filled_tank(computer_tank):
                if best_card == 'SOH':
                    opponent_tank = int(opponent_tank / 2)
                elif best_card == 'DOT':
                    opponent_tank = 0
                elif best_card == 'DMT':
                    computer_tank *= 2
                    computer_tank = apply_overflow(computer_tank)
                # Draw a new power card from the pile
                new_card = get_card_from_pile(power_cards_pile, 0)

        # Print the card the computer player used
        print(f"Computer used card: {best_card}")

        # Add the new card to the computer's hand
        computer_cards.append(new_card)
        # Arrange the computer's cards
        arrange_cards(computer_cards)

    # Return the updated tank levels
    return (computer_tank, opponent_tank)



def main():
    """
    Main function to run the water tank game.
    Initializes the game, deals cards, and manages turns between human and computer players.
    """
    # Print gaming instructions and rules
    print("Water Tank is a competitive card game played between two players (Human vs Computer). Each player starts with an empty water tank, which they need to fill. The goal is to be the first player to fill their tank. A tank is filled if it reaches the value of 75 to 80 units (inclusive). The human player's moves are decided by the user playing the game, by asking for input, and the computer's moves are decided by the program that you will write.")

    # Initialize tank levels for human and computer
    human_tank = 0
    computer_tank = 0


    try:
        # Set up the water and power card piles
        water_cards_pile, power_cards_pile = setup_cards()
        
        # Deal cards to human and computer players
        human_cards, computer_cards = deal_cards(water_cards_pile, power_cards_pile)

        # Randomly decide who goes first
        player = random.randint(0, 1)
        if player == 0:
            print("Human player goes first.")
        else:
            print('Computer goes first.')

        # Main game loop
        while True:
            if player == 0:
                # Human player's turn
                human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, computer_tank)
                if filled_tank(human_tank):
                    print("Human player wins!")
                    break
                player = 1
            else:
                # Computer player's turn
                computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, human_tank)
                if filled_tank(computer_tank):
                    print("Computer player wins!")
                    break
                player = 0
                
            # Check and replenish piles if necessary
            check_pile(water_cards_pile, 'water')
            check_pile(power_cards_pile, 'power')
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
