#8) გააკეთეთ Sum Of Odd Numbers. მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ


num = [22, 1, 4, 5, 6, 9, 53, 44, 55, 99, 18, 11]

odd_num = 0

odd_num_list = []


for i in range(len(num)):
    if num[i] %2 != 0:
        odd_num += num[i]
        odd_num_list.append(num[i])

for i in range(10):
    print(odd_num)




