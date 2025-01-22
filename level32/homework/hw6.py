#6) გააკეთეთ Filter Odd Numbers. მიზანი: გაფილტრეთ 
# ყველრა კენტი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ


num = [33, 44, 54, 311, 66, 72, 99, 898, 577]


odd_num = []

for i in range(len(num)):
    if num[i] %3 == 0:
        odd_num.append(num[i])

print(odd_num)

