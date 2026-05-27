balance = float(input("Enter your account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount > 0:
        print("Withdrawal successful")
    else:
        print("Enter a valid amount")
else:
    print("Insufficient balance")
