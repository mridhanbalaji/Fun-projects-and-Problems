def searchInsertK(Arr, N, k):
    list1 = []
    greater_list = []
    final_list = []
    for i in Arr:
        list1.append(i)
    for i in Arr:
        if i > k:
            greater_list.append(i)
        
    testnumber = greater_list[0]
    for i in Arr:
        if i == testnumber:
            store = int(list1.index(i))
            final = store - 1
    if len(greater_list) == 0:
        return N
    else:
        for i in range(N):
            if Arr[i] == k:
                return i
            else:
                return final

searchInsertK({1, 3, 5, 6}, 4 ,5)