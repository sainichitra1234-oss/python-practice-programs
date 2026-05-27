age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

if age >= 17:
    if marks >= 60:
        print("Eligible for college admission")
    else:
        print("Not eligible due to low marks")
else:
    print("Not eligible due to age")
