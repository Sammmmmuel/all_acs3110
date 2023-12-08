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
    if len(items) > 1:
        left_items = items[:len(items)//2]
        right_items = items[len(items)//2:]

        merge_sort(left_items)
        merge_sort(right_items)

        i = 0
        j = 0
        k = 0

        while i < len(left_items) and j < len(right_items):
            if left_items[i] < right_items[j]:
                items[k] = left_items[i]
                i += 1 
            else:
                items[k] = right_items[j]
                j += 1 
            k+= 1

        while i < len(left_items):
            items[k] = left_items[i]
            i += 1
            k += 1

        while j < len(right_items):
            items[k] = right_items[j]
            j += 1 
            k += 1 

# items = [3,5,1,7,4,6,5,3,6]
# merge_sort(items)
# print(items)


def partition(items, low, high):
    i = low
    j = high - 1 
    pivot = items[high]

    while i < j:
        while i < high and items[i] < pivot:
            i += 1 
        while j > low and items[j] >= pivot:
            j -= 1 
        if i < j:
            items[i], items[j] = items[j], items[i]
    if items[i] > pivot:
        items[i], items[high] = items[high], items[i]
    return i

def quick_sort(items, low, high):
    if low < high:
        partition_pos = partition(items, low, high)
        quick_sort(items, low, partition_pos - 1)
        quick_sort(items, partition_pos + 1, high)


items = [3,5,1,7,4,6,5,3,6]
quick_sort(items, 0, len(items)-1)
print(items)