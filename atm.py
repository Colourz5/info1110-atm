import sys


def bal():
    global ERROR
    print("{} {}".format(first, last))
    print("BSB: {}".format(bsb))
    print("ACCNO: {}".format(accno))
    print("BALANCE: {:.2f}\n".format(balance))


def deposit():
    global balance
    global ERROR
    global SUCCESS
    try:
        fifty = int(input("How many 50's? "))
        twenty = int(input("How many 20's? "))
        ten = int(input("How many 10's? "))
        five = int(input("How many 5's? "))
        negative = fifty < 0 or twenty < 0 or ten < 0 or five < 0
        if negative:
            print(ERROR + "Invalid input, specify a positive number\n")
        else:
            totaldeposit = NOTES[0]*fifty + NOTES[1]*twenty + NOTES[2]*ten + NOTES[3]*five
            balance += totaldeposit
            print(SUCCESS + "deposited ${:.2f} into your account\n".format(totaldeposit))
    except TypeError:
        print(ERROR + "Invalid input, specify a positive number\n")


def withdraw(amount):
    global balance
    global ERROR
    global SUCCESS
    try:
        amount = float(amount)
        if amount < 0:
            print(ERROR + "Unable to withdraw amount, amount requested is invalid\n")
        elif balance - amount < 0:
            print(ERROR + "Unable to withdraw amount, amount requested is greater than balance.\n")
        else:
            balance -= amount
            print(SUCCESS + "Withdrew {:.2f} from account\n".format(amount))
    except TypeError:
        print(ERROR + "Unable to withdraw amount, amount requested is invalid\n")


def quit():
    print("Have a nice day!")
    sys.exit()


def cont():
    cont = input("Do you want to continue? Y/N ")
    if cont == "N":
        quit()


if __name__ == "__main__":
        ERROR = "ERROR: "
        SUCCESS = "SUCCESS: "
        try:
            first = sys.argv[1]
            last = sys.argv[2]
            bsb = sys.argv[3]
            accno = sys.argv[4]
            balance = float(sys.argv[5])
        except IndexError or TypeError:
            print(ERROR + "Not enough arguments supplied")
            sys.exit()
        NOTES = [50, 20, 10, 5]
        asking = True
        while asking:
            command = input()
            if command == "balance":
                bal()
            elif command == "deposit":
                deposit()
            elif command[:8] == "withdraw":
                amount = (command.split(" "))[1]
                withdraw(amount)
            elif command == "quit":
                quit()
            cont()
