# Code with print breakdown

# sortMe = [6,5,3,1,8,7,2,4]

# def insertionSort(list):
#     for idx in range (1,len(list)):
#         print('Starting list for outer loop',idx,list)
#         temp = list[idx]
#         print('Temp at index', idx, '=', temp)
#         print('Compare',temp,'&',list[idx-1])
#         while temp < list[idx-1] and idx > 0:
#             print('Move', list[idx-1],'to index', idx)
#             list[idx] = list[idx-1]
#             print('List after move', list)
#             idx -= 1
#         print(f'Insert temp ({temp}) at index {idx}')
#         list[idx] = temp
#         print('List after insert', list)
#         print('-'*80)
        
#     return list

# print(insertionSort(sortMe))


# Prints removed

# sortMe = [6,5,3,1,8,7,2,4]

# def insertionSort(list):
#     for idx in range (1,len(list)):
#         temp = list[idx]
#         if temp > list[idx-1]:
#             continue
#         while temp < list[idx-1] and idx > 0:
#             list[idx] = list[idx-1]
#             idx -= 1
#         list[idx] = temp
#     return list

# print(insertionSort(sortMe))


sortMe = [6,5,3,1,8,7,2,4]

def insertionSort(list):
    for idx in range (1,len(list)):
        temp = list[idx]
        while temp < list[idx-1] and idx > 0:
            list[idx] = list[idx-1]
            idx -= 1
        list[idx] = temp
    return list

print(insertionSort(sortMe))