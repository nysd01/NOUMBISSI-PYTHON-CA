def multiplication_table(number,limit):
    for i in range(1,limit + 1):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    num = int(input("Enter the number you want it's table of multiplication: "))
    ranges = int(input("Enter the range limits: "))
    multiplication_table(num, ranges)
    
    