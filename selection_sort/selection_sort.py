list = [8,5,2,6,9,3,1,4,0,7]

def selectionSort(list):
    for i in range(len(list)):
        minIdx = i
        for num in range(i,len(list)):
            if list[minIdx] > list[num]:
                minIdx = num
        list[i], list[minIdx] = list[minIdx], list[i]
    return list

print(selectionSort(list))
