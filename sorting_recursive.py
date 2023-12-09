#!python


# def merge(items1, items2):
#     """Merge given lists of items, each assumed to already be in sorted order,
#     and return a new list containing all items in sorted order.
#     TODO: Running time: ??? Why and under what conditions?
#     TODO: Memory usage: ??? Why and under what conditions?"""
#     # TODO: Repeat until one list is empty
#     # TODO: Find minimum item in both lists and append it to new list
#     # TODO: Append remaining items in non-empty list to new list

    
# def split_sort_merge(items):
#      """Sort given items by splitting list into two approximately equal halves,
#      sorting each with an iterative sorting algorithm, and merging results into
#      a list in sorted order.
#      TODO: Running time: ??? Why and under what conditions?
#      TODO: Memory usage: ??? Why and under what conditions?"""
#      # TODO: Split items list into approximately equal halves
#      # TODO: Sort each half using any other sorting algorithm
#      # TODO: Merge sorted halves into one list in sorted order

    
def merge_sort(items):
    if len(items) > 1:      # only starts working if the array is greater than 1 
        left_items = items[:len(items)//2]    #iterates from start to middle 
        right_items = items[len(items)//2:] # iterates from middle to end 

        merge_sort(left_items)      # when recursion starts 
        merge_sort(right_items)  # using the function for the both sides of the spliced array 

        i = 0   # keeping track of the left most elmnt in left array 
        j = 0 # keeping track of the left most elmnt of the right array
        k = 0     #keeping track of the merged array index 

        while i < len(left_items) and j < len(right_items): # iterating thoruhg array looking for the left most lemnt
            if left_items[i] < right_items[j]: # compares left array at index i to right array at inx j
                items[k] = left_items[i]   #saving value found from left arr in merged array
            else:
                items[k] = right_items[j]
                j += 1  #increasing i and j
            k+= 1

        while i < len(left_items):   #i is small bcuz of missing numbers in the other array 
            items[k] = left_items[i]  # comparing arrays 
            i += 1  #increasing both arrays 
            k += 1

        while j < len(right_items):   # if sorted but missing in right arr
            items[k] = right_items[j]  #all left over numbers are added to the merged array
            j += 1 
            k += 1 

# items = [3,5,1,7,4,6,5,3,6]
# merge_sort(items)
# print(items)


def partition(items, low, high):
    i = low  #defining num to the left of piv 
    j = high - 1 # defining num to the right of the piv 
    pivot = items[high]

    while i < j:  #checking if j is greater than i
        while i < high and items[i] < pivot:  #moving the num either i or j comparing to the pivot 
            i += 1  # right if increasing 
        while j > low and items[j] >= pivot:  #left decresing 
            j -= 1 
        if i < j:
            items[i], items[j] = items[j], items[i] #swapping numbers when i and j cross 
    if items[i] > pivot:
        items[i], items[high] = items[high], items[i] # swapping if the item i if greater than pivot
    return i # sending to quick sort def

def quick_sort(items, low, high):
    if low < high:      # checking if the sub arr contains at least 2 elmnts
        partition_pos = partition(items, low, high)     #calling our partition fun that returns piv after quicksort fun is used
        quick_sort(items, low, partition_pos - 1)  #calling sort if all elements are less than one 
        quick_sort(items, partition_pos + 1, high)  # calling is sort is greater than piv


items = [3,5,1,7,4,6,5,3,6]
quick_sort(items, 0, len(items)-1)
print(items)