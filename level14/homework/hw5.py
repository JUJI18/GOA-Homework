#5)შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.

num1 = int(input("enter number here:"))


num2 = int(input("enter second number here:"))

print(num1 >10)
print(num2 >10)
print(num1 <50)
print(num2 <50)


print(num1 >10 and num2 <50)
print(num2 >10 and num1 <50)