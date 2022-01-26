a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

maximum = a

if maximum < b and b > c:
    maximum = b
elif maximum < c:
    maximum = c


print(f"maximum number is {maximum}")




