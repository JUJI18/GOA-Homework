#1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი


user_number = int(input("დაწერე რიცხვი:"))

for i in range(1, user_number):
    user_number = user_number + i

print(user_number)