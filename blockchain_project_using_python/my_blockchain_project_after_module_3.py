# AFTER MODULE 3
MINNING_REWARD = 10

# initialising our  blockchain list
genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": []
}
blockchain = [genesis_block]
open_transactions = []
owner = "shahid"
participants = set()


def hash_block(block):
    return "_".join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"]
                  if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"]
                      for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_recipient = [[tx["amount"] for tx in block["transactions"]
                     if tx["recipient"] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved-amount_sent


def get_last_blockchain_value():
    """returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]

# this function accepts two arguments
# one required one (transaction_amount) and one optional one (last_transaction)
# the optional one is optional because it has a default value=> [1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """append  a new values as well as the last blockchain value to the blockchain

    arguments:
         sender: the sender of the coins
         recipient: the reciever of the coins
         amount: the number of the coins sent"""

    transaction = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = []
    hashed_block = hash_block(last_block)
    reward_transaction = {
        "sender": "MINNING",
        "recipient": owner,
        "amount": MINNING_REWARD

    }
    copied_transactiins = open_transactions[:]
    copied_transactiins.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactiins
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """returns the input of the user (a new transaction amount  as a float"""
    # get the user input, tranform it from a string to float and store it in user_input
    tx_recipient = input("enter the recipient of the transaction: ")
    tx_amount = float(input("your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    # prompts the user for choice and returns it
    user_input = input("your choice: ")
    return user_input


def print_blochchain_elements():
    # output the blockchain list to the console
    for block in blockchain:
        print("outputting block")
        print(block)
    else:
        print("_"*50)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index-1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    """  is_valid = True
    for tx in open_transactions:
        if verify_transaction(tx):
            is_valid = True
        else:
            is_valid = False

    return is_valid"""


waiting_for_input = True
while waiting_for_input:
    print("1: add a new element in the blockchain")
    print("2: mine a new block")
    print("3: output tht blockchain")
    print("4: output the numbers of participants")
    print("5: verify tansactions")
    print("h: hack the chain")
    print("q: quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("TRANSACTION SUCCESSFUL !")
        else:
            print("TRANSACTION FAILED !")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []

    elif user_choice == "3":
        print_blochchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "h":
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transaction": [{"sender": "sahil", "recipient": "suhail", "amount": 1000000.0}]
            }
    elif user_choice == "q":

        waiting_for_input = False

    elif user_choice == "5":
        if verify_transactions():
            print(" all transactions are valid ")
        else:
            print("there are some invalid transactions")

    else:
        print("invalid input , please pick a value from the list!")

    if not verify_chain():
        print_blochchain_elements()
        print("invalid blockchain!")
        break
    print(get_balance("shahid"))
else:
    print("user left")
