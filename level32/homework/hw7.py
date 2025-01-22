#7) გააკეთეთ Sum Of Even Numbers. მიზანი: შეკრიბეთ ყველა ლუწი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ


num = [22, 33, 12, 78, 4, 5, 67, 66, 787, 332, 444]

even_sum = 0

for i in range(len(num)):
    if num[i] % 2 == 0: 
        even_sum += num[i] 

for _ in range(10):
    print(even_sum) 