r1 = int(input("Enter the range 1: "))
r2 = int(input("Enter the range 2: "))
i = int(input("Enter the number of lines: "))

numbers = []

for x in range(0,i):
    num = int(input(""))
    numbers.append(num)

print("\n\n\n\nRESULTS ARE: ")

for y in range(r1, r2+1):
    if y not in numbers:
        print(y)