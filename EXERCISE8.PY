def sum_of_cubes(number_limits):
    sum_cubes = 0
    for i in range(1, number_limits ):
        cubes = i ** 3
        sum_cubes = sum_cubes + cubes
    return sum_cubes
if __name__ =="__main__":
    number = int(input("Enter the number limit to start cubes: "))
    result = sum_of_cubes(number)
    print(f'the sum of cubes is: {result}')        
