if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    set_arr = set(arr) # to store unique items of the array
    list_arr = list(set_arr) # to convert it to list
    list_arr.sort() # to sort the list so that we can access the last second item
    
    print(list_arr[-2])
    
