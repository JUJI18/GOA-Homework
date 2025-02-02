#4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს შემდეგ კი მათ გამოაკლებს ერთმანეთს 


def numbers():
    num1 = int(input("Enter number here:"))
    num2 = int(input("Enter second number here:"))
    print(num2 - num1)
    print(num1 - num2)


numbers()