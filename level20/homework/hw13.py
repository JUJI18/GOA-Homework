# while loop  ის დახმარებით შეიყვანეთ რიცხვი და დაბეჭდეთ ყველა რიცხვი, რომელიც გაცილებით მეტი ან ნაკლებია 10-ზე.

while True:
        numerro = int(input("დაწერე რიცხვი აქ:"))
        if numerro < 10:
            print(str(numerro)+ " ეს რიცხვი ნაკლებია 10-თან შედარებით")
        elif numerro > 10:
            print(str(numerro)+ " რიცხვი 10-ზე მეტია")
