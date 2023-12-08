#!python


def counting_sort(numbers):
    min_val = min(numbers)  #looking for min value
    max_val = max(numbers)  #looking for max value 

    count_num = [0 for i in range(min_val, max_val + 1)] # array thats keeping count of numbers and setting all index number to zero to all numbers between min and max 
    for value in numbers: # passing through the array
        index = value - min_val # setting the index to zero 
        count_num[index] += 1 

    sorted_num = [] 
    for index, item in enumerate(count_num): 
        sorted_num.extend([index + min_val] * item)
    return sorted_num

# numbers = [4,2,3,8,5,4,1,4,8]
# sorted_numbers = counting_sort(numbers)
# print(sorted_numbers)


def bucket_sort(numbers):
    bucket = []

    for i in range(len(numbers)):  # creating a bunch of empty buckets 
        bucket.append([])
    
    for j in numbers:           # putting numbers into buckets
        index = int(10 * j)
        bucket[index].append(j)

    for i in range(len(numbers)):   # sorting the elements inside the buckets 
        bucket[i] = sorted(bucket[i])
    
    k = 0           # getting the elements that have been sorted
    for i in range(len(numbers)):
        for j in range(len(bucket[i])):
            numbers[k] = bucket[i][j]
            k += 1
    return numbers

numbers = [.32, .22, .23, .42, .27, .37, .41]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)
