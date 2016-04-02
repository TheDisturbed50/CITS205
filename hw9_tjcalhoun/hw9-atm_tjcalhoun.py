# Thomas Calhoun
# homework #9
# tjcalhoun@alaska.edu  31 Mar 2016
# Python 3.5.1

"""
Calhoun Banking.

Watching your money, so you don't have to!
"""

#######################################################################################################################
#  Definition of some menu text to keep function lines at a minimal
#######################################################################################################################

menuTitle = 'Calhoun Banking Terminal'
menuText = '''
Please use the number keys to select from one of the following:

1 - Check Balance
2 - Withdraw Funds
3 - Deposit Funds
4 - Transfer Funds

0 - Logoff
'''

#######################################################################################################################
#  Global Variable pool
#######################################################################################################################

savingsBalance = 10000.00
checkingBalance = 1000.00
bankAccounts = {1337: "-notset-"}
acctGet = 0

#######################################################################################################################
#  Definition of the Deposit Funds function
#######################################################################################################################


def deposit():  # Deposit, Withdraw, and Transfer, are varied copies of the following.
    """
    Deposit Funds
    Where does it come from?

    The cloud, man... The cloud.
    """
    global savingsBalance, checkingBalance
    print("\n\nPlease select the account to deposit TO:\n(C) - Checking\n(S) - Savings\n")
    while True:  # Had to enforce this with a loop to control incorrect input
        askfracct = input("Selection >>> ").lower()
        if askfracct == "c":  # Conditional sets a local variable for chosen account.
            dep = checkingBalance
            print("\n", "Checking Account selected...".center(80))
            break
        elif askfracct == "s":
            dep = savingsBalance
            print("\n", "Savings Account selected...".center(80))
            break
        else:
            print("\nChoice not recognized, please try again!\n")
    while True:
        print("\n\n(Type in an amount of \"000\" to cancel)\n\n")
        amt = float(input("Amount of funds to transfer: $"))
        if amt == 000:
            print("\n\n\n", "--==WITHDRAWAL CANCELLED==--".center(80), "\n\n\n")
            main()
        else:
            break

    if askfracct == "c":  # this conditional reassigns out local variable with calculations to the global variable.
        checkingBalance = dep + amt
    elif askfracct == "s":
        savingsBalance = dep + amt

    print("Withdrawal complete...")
    print("\n    Account Summary for {}:".format(bankAccounts[acctGet]))
    print("\nChecking: %.2f" % checkingBalance)  # Getting the float formatting to work meant breaking apart each line
    print("Savings: %.2f\n\n" % savingsBalance)

#######################################################################################################################
#  Definition of the Withdraw Funds function
#######################################################################################################################


def withdraw():
    """
    Withdraw Funds.
    Note: No actual money will come out of your computer.
    Not even Bitcoin.

    I tried, and then cried myself to sleep.
    *sniff* Oh no... here we go again...
    """
    global savingsBalance, checkingBalance
    print("\n\nPlease select the account to withdraw FROM:\n(C) - Checking\n(S) - Savings\n")
    while True:
        askfracct = input("Selection >>> ").lower()
        if askfracct == "c":
            wdraw = checkingBalance
            print("\n", "Checking Account selected...".center(80))
            break
        elif askfracct == "s":
            wdraw = savingsBalance
            print("\n", "Savings Account selected...".center(80))
            break
        else:
            print("\nChoice not recognized, please try again!\n")
    while True:
        print("\n\n(Type in an amount of \"000\" to cancel)\n\n")
        amt = float(input("Amount of funds to transfer: $"))
        if amt > wdraw:
            print("\n\n  ###  Error! Insufficient Funds...  ###")
        elif amt == 000:
            print("\n\n\n", "--==WITHDRAWAL CANCELLED==--".center(80), "\n\n\n")
            main()
        else:
            break

    if askfracct == "c":
        checkingBalance = wdraw - amt
    elif askfracct == "s":
        savingsBalance = wdraw - amt

    print("Withdrawal complete...")
    print("\n    Account Summary for {}:".format(bankAccounts[acctGet]))
    print("\nChecking: %.2f" % checkingBalance)
    print("Savings: %.2f\n\n" % savingsBalance)

#######################################################################################################################
#  Definition of the Transfer Funds function
#######################################################################################################################


def transfer():
    """
    Transfer Funds.
    Think of it as shuffling cards, just only with your
    hard earned money.

    At least it doesnt say "Read em' and weep!"
    """
    global checkingBalance, savingsBalance
    print("\n\nPlease select the account to transfer FROM:\n(C) - Checking <TO> Savings\n"
          "(S) - Savings <TO> Checking\n")
    while True:
        askfracct = input("Selection >>> ").lower()
        if askfracct == "c":
            wdraw = checkingBalance
            dep = savingsBalance
            print("\n", "Checking -to- Savings Account selected...".center(80))
            break
        elif askfracct == "s":
            wdraw = savingsBalance
            dep = checkingBalance
            print("\n", "Savings -to- Checking Account selected...".center(80))
            break
        else:
            print("\nChoice not recognized, please try again!\n")
    while True:
        print("\n\n(Type in an amount of \"000\" to cancel)\n\n")
        amt = float(input("Amount of funds to transfer: $"))
        if amt > wdraw:
            print("\n\n  ###  Error! Insufficient Funds...  ###")
        elif amt == 000:
            print("\n\n\n", "--==TRANSFER CANCELLED==--".center(80), "\n\n\n")
            main()
        else:
            break

    if askfracct == "c":
        checkingBalance = wdraw - amt
        savingsBalance = dep + amt
    elif askfracct == "s":
        savingsBalance = wdraw - amt
        checkingBalance = dep + amt

    print("Withdrawal complete...")
    print("\n    Account Summary for {}:".format(bankAccounts[acctGet]))
    print("\nChecking: %.2f" % checkingBalance)
    print("Savings: %.2f\n\n" % savingsBalance)

#######################################################################################################################
# Definition of the Main Menu
#######################################################################################################################


def main():
    """
    The Driving force of most programs and restaurants...
    The Menu!
    """
    global savingsBalance,checkingBalance
    while True:
        print("\n\n", "...MAIN MENU...".center(80), "\n\n", menuText)
        sel = int(input("Selection >>>  "))
        if sel == 0:
            print("\n\n","Logoff Successful...".center(80), "\n", "Have a nice day!".center(80))
            break
        elif sel == 1:  # A short snippet of code is all that is required for this option
            print("\n    Account Summary for {}:".format(bankAccounts[acctGet]))
            print(
                "\nChecking: %.2f" % checkingBalance)
            print("Savings: %.2f\n\n" % savingsBalance)
        elif sel == 2:
            withdraw()
        elif sel == 3:
            deposit()
        elif sel == 4:
            try:
                transfer()
            except ValueError:
                print("\n\nUh Oh!\nOnly numbers will be recognized as input.\n-Please try again!\n\n")
                transfer()
            except Exception as err:
                print("\n\nUh Oh! A {} Error Occurred!\nThis may have happened because of incorrect input."
                      "\n-Verify your response before pressing <Enter>. Please try again!\n\n".format(err))
                transfer()
        else:
            print("\n\nSorry! Input not recognized, please choose from the following menu options!\n\n")

#######################################################################################################################
# Call to initiate program
#######################################################################################################################
if __name__ == '__main__':

    # Why so many functions? Error Handling. If I call the target function again once it's handled an error,
    #     I've noticed that another exception afterward may not get handled...
    #     So, in its own function - it operates as a crude loop (at least that's how I picture it).
    # Please reference the docstring for each function to understand my interpretation of it pythonic flow. Heh.

    def start():
        """
        Start Function initiates the Main Menu, only after
        Account Authentication has taken place.
        Error handling in place for a secure start.
        """
        try:
            main()
        except ValueError:
            print("\n\nUh Oh!\nOnly numbers will be recognized as input.\n-Please try again!\n\n")
            start()

    def acct():
        """
        Account Function screens the user for login credentials.
        Since security is our topmost priority, we only require
        your account number (which may or may not resemble a
        classic Pixar movie easter egg reference).
        """
        global bankAccounts, acctGet
        while True:
            print(menuTitle.center(80),"\n\n", "Welcome! Please log in...".center(80), "\n\n")
            acctGet = int(input("User Account Number  >>> "))
            if acctGet in bankAccounts.keys():  # may try 'if acctGet in bankAccounts.keys():'
                if bankAccounts[acctGet] == "-notset-":  # Name prompt, for user to set up their account.
                    nSet = input("\n\nWelcome, this is your first login, so please type your full name!\n"
                                 "Name: ").title()
                    bankAccounts[acctGet] = nSet  # Saves account name.
                    print("\n\nHello {}! Thank you for choosing Calhoun Banking!\n\n".format(bankAccounts[acctGet]))
                print("Welcome {}!".format(bankAccounts[acctGet]))
                break
            else:
                print("\n\nAccount was not found... please try again!\n\n")

        start()

    def acct_handler():
        """
        Account Handler Function is the error control method,
        just in case someone decides "casablanca" would be a
        good account to guess into (it's not).
        """
        try:
            acct()
        except KeyError:  # Since I'm using a dict to hold account info
            print("\n\nAccount was not found... please try again!\n\n")
            acct_handler()
        except ValueError:  # Since account input is a forced integer
            print("\n\nYou needed to type a number... please try again!\n\n")
            acct_handler()

    # The line starts it all.
    acct_handler()
