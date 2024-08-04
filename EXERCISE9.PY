def find_max_min(sequence):
    maximum = sequence[0]
    minimum = sequence[0]
    for i in sequence:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i   
    return(f'maximum: {maximum} , minimum: {minimum}')

    
if __name__ == "__main__":
    seq =[2,4,12,6,7,9,21,4,21,54]
    result = find_max_min(seq)   
    print(result)       