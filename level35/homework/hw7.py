# 7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი



def numbers():
    num1 = int(input("Enter number here:"))
    if num1 %2 == 0:
        print("ლუწი რიცხვია")
    elif num1 %2 != 0:
        print("კენტი რიცხვია")


numbers()