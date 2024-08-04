def compare():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    unique =[]
    for item in color_list_1:
        if item not in color_list_2:
            unique.append(item)
    return unique

if __name__ =="__main__":
    result = compare()        
    print(result)