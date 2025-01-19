#4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი 
# ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ 5 ის ჯერადი რიცხვების ჯამი ცალკე და მხოლოდ 3ის ჯერადი რიცხვების ჯამი ცალკე, გამოიყენეთ while loop

user_number = int(input("დაწერეე რიცხვიი აქქ:"))

xutis= 0
samis = 0

i = 0

while i < user_number:
    if i % 5 == 0:
        xutis = xutis + i
    elif i % 3 == 0:
        samis = samis + i
    
    i = i + 1

print(xutis)
print(samis)