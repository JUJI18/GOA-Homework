# 12) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა კენტ რიცხვს


def user_num():
    num = int(input("დაწერე რიცხვი:"))
    for i in range(1, num, 2):
        print(i)

user_num()