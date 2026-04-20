# initialising our  blockchain list
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]
    """returns the last value of the blockchain."""


def add_value(transaction_amout, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amout])
    """append  a new values as well as the last blockchain value to the blockchain
     
      arguments:
         :transaction_amount: the amount that should be added.
         :last_transaction: the last blockchaun transaction (default[1]). """


def get_user_input():
    return float(input("your transaction amount please:"))
    """returns the input of the user (a new transaction amount  as a float"""


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amout=tx_amount)
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)


# [0]-[positive]  accessing the list from the left
# [-1]-[negative] accessing the list from the right
