
number = int(input("Enter the size of the pattern: "))
row = 1
while row <= number:
    for i in range(1, number+1):
        print("*", end="")
        print()
        row += 1
