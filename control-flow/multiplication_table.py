number = int(input("Enter a number to see its multiplication table: "))
print(f"\nMultiplication table for {number}:")

for x in range(1, 11):
        product = number * x
        print(f"{number} * {x} = {product}")
