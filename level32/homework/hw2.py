#2) გააკეთეთ Reverse List და გამოიყენეთ while loop.
#  შემოაბრუნეთ ყველა რიცხვი ლისტში. ახსნა: [1, 2, 3, 4,  5] => [5, 4, 3, 2, 1]


num = [1,2,3,4,5]



reversed_num = []

i = len(num) -1

while i >= 0:
    reversed_num.append(num[i])
    i -=1

print(reversed_num)


