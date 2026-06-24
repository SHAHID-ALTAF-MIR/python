
# AFTER MODULE 2
# by using loops in this project we will verify our blockchain


# initialising our  blockchain list

blockchain = []


def get_last_blockchain_value():
    """returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# this function accepts two arguments
# one required one (transaction_amount) and one optional one (last_transaction)
# the optional one is optional because it has a default value=> [1]


def add_transaction(transaction_amout, last_transaction=[1]):
    """append  a new values as well as the last blockchain value to the blockchain

    arguments:
         :transaction_amount: the amount that should be added.
         :last_transaction: the last blockchain transaction (default[1]). """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amout])


def get_transaction_value():
    """returns the input of the user (a new transaction amount  as a float"""
    # get the user input, tranform it from a string to float and store it in user_input
    user_input = float(input("your transaction amount please: "))
    return user_input


def get_user_choice():
    user_input = input("your choice: ")
    return user_input


def print_blochchain_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print("outputting block")
        print(block)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

    #   block_index = 0
    #   is_valid = True
    #   for block in blockchain:
    #       if block_index == 0:
    #           block_index += 1
    #           continue
    #       elif block[0] == blockchain[block_index - 1]:
    #           is_valid = True
    #       else:
    #           is_valid = False
    #           break
    #       block_index += 1
    # return is_valid


waiting_for_input = True
while waiting_for_input:
    print("please choose")
    print("1: add a new element in the blockchain")
    print("2: output tht blockchain")
    print("h: manipulate the chain")
    print("q: quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blochchain_elements()
    elif user_choice == "q":
        print("quitting the program as requested")
        waiting_for_input = False
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    else:
        print("invalid input , please pick a value from the list!")

    if not verify_chain():
        print("invalid blockchain!")
        break
else:
    print("closed")
print("done")
