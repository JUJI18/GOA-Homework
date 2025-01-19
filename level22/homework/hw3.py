#3) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის კვადრატის ჯამი


user_number = int(input("დაწერე რიცხვი აქ:"))


if user_number > 0:
    sum = 0
    for i in range(1, user_number):
        sum += i ** 2
    print(sum)
else:
    print("რიცხვი ტოლია ნულის ან ნაკლებია ნულზე!")