def BinarySearch(array,binary):
    first = 0
    last = len(array)-1
    Found = False
    
    while first <= last and not Found:
        mid = (first+last)//2
        if binary == array[mid]:
            Found = True
        elif binary > array[mid]:
            first = mid+1
        else:
            last = mid-1
    if Found == True:
        print("1")
    else:
        print("0")

array = [4,7,9,13,16,18,20]
print(array)
binary = int(input("enter the number"))
BinarySearch(array,binary)