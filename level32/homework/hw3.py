#3) გააკეთეთ Filter Even Numbers. მიზანი: 
# გაფილტრეთ ყველრა ლუწი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ



my_list = [12, 33, 46, 76, 41, 20, 98, 57, 39, 100]


even_num = []

for i in range(len(my_list)):
    if my_list[i] %2 == 0:
        even_num.append(my_list[i])

print(even_num)