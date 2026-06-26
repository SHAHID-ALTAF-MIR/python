# AFTER MODULE 5
from functools import reduce
import hashlib as hl
import json
from collections import OrderedDict
MINNING_REWARD = 10

# initialising our  blockchain list
genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
    "proof": 100
}
blockchain = [genesis_block]
open_transactions = []
owner = "shahid"
participants = set()


def hash_block(block):
    """Hashes a block using SHA-256 and returns the hex digest.

    Arguments:
        block: the block to be hashed."""
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


def valid_proof(transactions, last_block, proof):
    """Validates a proof of work by checking if the hash starts with '00'.

    Arguments: 
        transactions: the current open transactions.
        last_block: the hash of the last block.
        proof: the proof number to validate."""
    guess = (str(transactions)+str(last_block) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == "00"


def proof_of_work():
    """Finds and returns a valid proof of work for the current open transactions."""
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    """Calculates and returns the balance of a given participant.

    Arguments:
        participant: the person whose balance is being calculated."""
    tx_sender = [[tx["amount"] for tx in block["transactions"]
                  if tx["sender"] == participant] for block in blockchain]
    open_tx_sender = [tx["amount"]
                      for tx in open_transactions if tx["sender"] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum, tx_sender, 0)
    tx_recipient = [[tx["amount"] for tx in block["transactions"]
                     if tx["recipient"] == participant] for block in blockchain]
    amount_recieved = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum, tx_recipient, 0)
    return amount_recieved-amount_sent


def get_last_blockchain_value():
    """returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    """Verifies that the sender has sufficient balance for the transaction.

    Arguments:
        transaction: the transaction dict containing sender, recipient, and amount."""
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
    transaction = OrderedDict(
        [("sender", sender), ("recipient", recipient), ("amount", amount)])
    # transaction = {
    #    "sender": sender,
    #   "recipient": recipient,
    #    "amount": amount
    # }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """Mines a new block by finding a valid proof and adding it to the blockchain."""
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = OrderedDict(
        [("sender", "MINNING"), ("recipient", owner), ("amount", MINNING_REWARD)])
    # reward_transaction = {
    #   "sender": "MINNING",
    #   "recipient": owner,
    #   "amount": MINNING_REWARD
    # }
    copied_transactiins = open_transactions[:]
    copied_transactiins.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactiins,
        "proof": proof
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
    """Prompts the user for a menu choice and returns it."""
    user_input = input("your choice: ")
    return user_input


def print_blochchain_elements():
    """Outputs all blocks in the blockchain to the console."""
    for block in blockchain:
        print("outputting block")
        print(block)
    else:
        print("_"*50)


def verify_chain():
    """Verifies the current blockchain and returns True if valid, False otherwise."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index-1]):
            return False
    return True


def verify_transactions():
    """Verifies all open transactions and returns True if all are valid."""
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True
while waiting_for_input:
    print("1: add a new element in the blockchain")
    print("2: mine a new block")
    print("3: output the blockchain")
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
    print("balance of {}: {:^6.2f}".format("shahid", get_balance("shahid")))
else:
    print("user left")
