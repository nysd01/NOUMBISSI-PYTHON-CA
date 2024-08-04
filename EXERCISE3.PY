def celsuis_to_fahreinheit(temp):
    convertion = temp * (9/5) + 32
    return convertion

if __name__ =="__main__":
    temperature = float(input("Enter temperature in celsius: "))
    result = celsuis_to_fahreinheit(temperature)
    print(f"{temperature} degree celcuis equal {result} fahrenheit")