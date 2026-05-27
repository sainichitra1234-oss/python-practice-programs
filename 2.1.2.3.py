years = int(input("Enter years of service: "))
salary = float(input("Enter your salary: "))

if years >= 5:
    if salary >= 30000:
        print("Employee is eligible for bonus")
    else:
        print("Not eligible due to low salary")
else:
    print("Not eligible due to less experience")
