marks = float(input("Enter your marks: "))
income = float(input("Enter family income: "))

if marks >= 85 and income <= 300000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
