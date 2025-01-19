#5) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ნამრავლი


user_number = int(input("დაწერე რიცხვი აქქ ==>:"))


if user_number > 0:
    for i in range(1, user_number):
        user_number = user_number * i

print(user_number)