def checking(sequence):
    for i in sequence:
        for j in sequence:
            if (i * j) % 2 != 0 and i != j:
                print(i,j)

if __name__ =="__main__":
    seq = [1,2,3,4,5,6,7,8,9,10]
    result = checking(seq)
    print(result)