#4) გააკეთეთ Find Maximum და გამოიყენეთ for loop. 
# მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]


num = [22, 1, 45, 77, 443, 339, 604, 14]

max_num = num[0]


for i in range(len(num)):
    if num[i] > max_num:
        max_num = num[i]  

print(max_num)







