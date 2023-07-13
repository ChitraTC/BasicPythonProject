sal=int(input("Enter your salary:"))
ser=float(input("Enter your total years of experience:"))

if ser>5:
    bonus=((5*sal)/100)
    print("New salary=",sal+bonus)

else:
    print("No bonus provided")