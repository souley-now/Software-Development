# Souleymane Diallo
# PennID: 63283765
# I worked alone on this assignment

# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# constants
constant_lottery_unit_price = 2 # unit price of a lottery ticket
constant_apple_unit_price = .99 # unit price of an apple
constant_canned_beans_unit_price = 1.58 # unit price of a can of beans
constant_soda_unit_price = 1.23 # unit price of a soda


# variables
money = 5 # money available
money_spent = 0 # the user has spent $0 initially
winnings = 0 # Winnings
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0 # initiate variable to track item counts


def get_user_input(prompt): 
    """This function return a string of a user input whether they want to purchase a given item"""
    return str(input(prompt)).upper() # return input in uppercase

def purchases(item_name, unit_price, amount):
    """This function calculates the purchases of a given item and returns the amount bought"""
    global money, money_spent  # declare money and money_spent as global variables
    total_amount = unit_price * amount  # calculate the total cost of the item

    if money < total_amount:  # check whether the user has enough money for the purchase
        print(f'Not enough money for {amount} {item_name}(s)! No {item_name} purchased\n')  # print a message if the user does not have enough money
    else:
        money -= total_amount  # reduce the cost of the item from the total money
        money_spent += total_amount  # track the cost of the items by adding to the total money spent
        print(f'You want to buy {amount} {item_name}(s). It will cost ${total_amount:.2f}') # desired amount and cost
        print(f'{amount} {item_name}(s) were purchased.\n{'--' * 30}') # print the puchased amount and item name
    return amount # return the number of items bought

def buy_lottery_ticket():
    """This function return compute whether the a given lottery ticket is a winner when you user agree to purchase a ticket.
    And reduce the total money available while tracking the money spent then print the number of tickets purchased and money left"""

    global money, money_spent, winnings, lottery_amount # declare money, money_spent, winnings, lottery_amount as global variables
    lottery_amount += 1 # increase the number of lottery ticket purchased by 1
    money -= constant_lottery_unit_price # reduce to total money available by the cost of the ticket
    money_spent += constant_lottery_unit_price # increase the total money spent

    if random.randint(0,2) == 0: # check whether the ticket win
        win_amount = random.randint(2, 10) # generate the winning number
        winnings += win_amount # add the winning amount to winnings
        money += win_amount # increase the total money by the winned amount
        print(f"Congratulations! You won ${win_amount}. You now have ${money:.2f}.") # display a congratualtion along with the winned amount with the total money available
    else:
        print("Sorry, you didn't win anything.") 
    print(f"You have bought {lottery_amount} lottery ticket(s) and have ${money:.2f} left\n") # display number of tickets boughts and money available

def buy_item(item_name, unit_price):
    """This function gets user input of the number of item they want to buy for a given item and compute then uses the purchases function to compute the cost and remaining amount of money"""

    global money, apple_amount, canned_beans_amount, soda_amount# declare canned beans amount as a global variable
    user_input = get_user_input(f'Would you like to buy {item_name}(s)? y/n: ') # get user input whether they want to buy a specific item
    if user_input == 'Y': 
        # use try and except block to catch errors
        try:
            amount = int(input(f'How many {item_name}(s) would you like to buy? ')) # get the amount of a given item 
            purchased_amount = purchases(item_name, unit_price, amount) # return the amount purchased of a given item            
            if purchased_amount > 0: # check if the value is greater than zero
                cost = purchased_amount * unit_price
                if cost < money:
                    if item_name == 'apple':
                        apple_amount += purchased_amount # add count to apple amount if the item is apple
                    elif item_name == 'canned beans': 
                        canned_beans_amount += purchased_amount # add count to canned bean amount if the item is canned bean
                    elif item_name == 'soda':
                        soda_amount += purchased_amount # add count to soda mount if the item is soda
        except: # catch the error
            print(f'Integer values only! No {item_name} selected.') # return a message about the error
    else:
        print(f'No {item_name}(s) were purchased.') 

def main():
    global money # declare money as a global variable
    # print greetings and items available for purchases
    print(f"\nWelcome to the supermarket! Here is what we have in stock:\n"
          f"1. Lottery ticket: ${constant_lottery_unit_price} each\n"
          f"2. Apple: ${constant_apple_unit_price} each\n"
          f"3. Can of beans: ${constant_canned_beans_unit_price} each\n"
          f"4. Soda: ${constant_soda_unit_price} each\n")

    # display total money available and price of lottery ticket
    print(f"You have ${money} available\nFirst, would you like to buy a ${constant_soda_unit_price} lottery ticket?")
    
    # get user input
    user_input = get_user_input('Please enter (y/n): ')
    if user_input == 'Y':
        buy_lottery_ticket() # call the lottery function
    else:
        print('No lottery tickets were purchased')
    
    print(f'You have ${money:.2f} available for purchases') # display total money remaining
    
    buy_item('apple', constant_apple_unit_price) # ask user if they want to buy apples

    print(f'You have ${money:.2f} available for purchases')
    
    buy_item('canned beans', constant_canned_beans_unit_price) # ask a user if they want to buy canned beans

    print(f'You have ${money:.2f} available for purchases') 
    
    buy_item('soda', constant_soda_unit_price) # ask user if they want to buy soda
    
    # display a receipt with the total money remaining
    print(f'Money left: ${money:.2f}\n'
          f'Lottery tickets purchased: {lottery_amount}\n'
          f'Lottery winnings: ${winnings}\n'
          f'Apple(s) purchased: {apple_amount}\n'
          f'Can(s) of Bean purchased: {canned_beans_amount}\n'
          f'Soda(s) purchased: {soda_amount}\n'
          f'Good Bye, have a nice day!!\n')

# run the program
if __name__ == "__main__":
    main()