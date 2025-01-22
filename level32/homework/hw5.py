#5) გააკეთეთ Find Minimum და გამოიყენეთ for loop. მიზანი: 
# სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]


num = [1, 4, 5, 6, 44, 3, 43, 23, 77]

minimum_num = num[0]



for i in range(len(num)):
    if num[i] < minimum_num:
        minimum_num = num[i]
        
print(minimum_num)
