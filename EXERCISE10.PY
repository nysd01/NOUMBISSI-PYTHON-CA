def check_divisibility(number1,number2):
    if number1 % number2  == 0:
        print(f"yes, number {number1} is divisible by number {number2}")
    else:
        print(f"no, number {number1} is not divisible by number {number2}")

if __name__ =="__main__":
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    result = check_divisibility(num1,num2)
    print(result)