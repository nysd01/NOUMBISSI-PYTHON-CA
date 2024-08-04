def decimalconverter(deci_num, mylist = None):
    if mylist is None:
        mylist =[]
    
    if deci_num == 0:
       return mylist[::-1]
    remainder = deci_num % 2
    mylist.append(remainder) 
    return decimalconverter(deci_num // 2,mylist)
      

if __name__ == "__main__" :
    number = int(input("enter a decimal number: "))
    result = decimalconverter(number)  
    print(result)