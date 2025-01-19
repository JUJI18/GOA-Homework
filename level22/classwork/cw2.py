#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop

user_number = int(input("დაწერე რიცხვი აქქ:"))


num =0

for i in range(user_number):
    if i % 2 == 0:
        num = num + i

print(num)