#Boss Level: გახსენით მაღაზია სახელად PC Parts, სადაც შეგიძლიათ შეიძინოთ სხვადასხვა კომპიუტერული ნაწილი მაგალითად: 
# პროცესორები, ვიდეო ბარათები, ოპერატიული მეხსიერება, კვების ბლოკები, კორპუსები და სხვა. თითოეულ პროდუქტს მიანიჭეთ 
# შესაბამისი ფასი. საბოლოოდ, დაპრინტეთ ჩეკი, სადაც ჩამოთვლილი იქნება შეძენილი ნივთები და ჯამური თანხა. 


user_hello =("მოგესალმებით💚! აირჩიეთ სასურველი პროდუქტი ციფრების მიხედვით⬇️:")
print(user_hello)


budget = 5000

items = []


while True:
    product = input("ლეპტოპი💻 [1], ყურსასმენი🎧 [2], კლავიატურა⌨️ [3], მაუსი🖱️ [4];")
    if product == "1":
        price = 3000
        if budget > price:
            items.append("ლეპტოპი💻")
            budget -= price
        print("თქვენ შეიძინეთ ლეპტოპი💻. ბალანსი:"+ " "+ str(budget))
    


    elif product == "2":
        price = 199
        if budget > price:
            items.append("ყურსასმენი🎧")
            budget -= price
        print("თქვენ შეიძინეთ ყურსასმენი🎧. ბალანსი:" + " "+ str(budget))
    elif product == "3":
        price = 300
        if budget > price:
            items.append("კლავიატურა⌨️")
            budget -= price
        print("თქვენ შიძინეთ კლავიატურა⌨️. ბაალანსი" + " "+ str(budget))
    elif product == "4":
        price = 167
        if budget > price:
            items.append("მაუსი🖱️")
            budget -= price
        print("თქვენ შეიძინეთ მაუსი🖱️. ბალანსი"+ " "+ str(budget))
    else:
        print("no")
