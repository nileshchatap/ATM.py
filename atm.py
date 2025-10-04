
print("Wellcome to ATM ".center(50))
balance = 20000000  # starting balance

while True:   # repeat until exit
    print("\n1) BALANCE\n2) WITHDRAW\n3) DEPOSIT\n4) EXIT")
    option = int(input("Choose: "))

    if option == 1:   # check balance
        print("Balance:", balance)

    elif option == 2:   # withdraw money
        atm = float(input("Withdraw: "))
        balance -= atm
        print("Successfully Withdraw")
        print("Current Balance:", balance)

    elif option == 3:   # deposit money
        atm = float(input("Deposit: "))
        balance += atm
        print("Successfully Deposit")
        print("Current Balance:", balance)

    elif option == 4:   # exit program
        print("Thank you Goodbye!")
        break
    else:
        print("invalid data,try again")
