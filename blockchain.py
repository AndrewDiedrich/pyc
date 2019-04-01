# initializing our empty blockchain list
blockchain = []
open_transactions = []
owner = 'Andrew'

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        """ Returns nothing if no previous value """
        return None
        #implicit else statement -1 will return if false
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Appends a new vlaue as well as the last block 

    Arguments:
        :sender: The sender of coins.
        :recipient: The recipient of the coins.
        :amount: The amout of coins being sent (default = 1).
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)

# pass doesn't do anything but doesn't return error either.
def mine_block():
    pass

def get_transaction_value():
    """ Returns the input of the transaction as a float"""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


    # Output the blockchain list to the console
def print_blockchain_elements():
    for block in blockchain:
        print('outputting block')
        print(block)
    else:
        print('-' * 20)


# Check to see if first block in chain is = to previous blockchain
def verify_chain():
    #block_index = 0
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


waiting_for_input = True

#tx loop transactions 
while waiting_for_input:
    print('Please Choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # unpack tuple ""
        recipient, amount = tx_data
        # add transaction to blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User Left')



print('Done')


