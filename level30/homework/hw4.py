#4) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, 
# შეამოწმეთ რიცხვი ლუწია თუ კენტი და თუ ლუწია დაამატეთ ახალ ლისტში



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


list2 = []

for i in my_list:
    if i %2 != 0:
        print("კენტი")
    elif i %2 == 0:
        list2.append(i)
        print("ლუწი", list2)










































































































