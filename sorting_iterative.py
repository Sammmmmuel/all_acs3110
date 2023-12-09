#!python


def is_sorted(items):
    if len(items) in [0, 1]:
        return True
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    for i in range(len(items)-1,0,-1):  #getting len of list with outer loop 
        for j in range(i):    # looking for the biggest number and comparing to the other numbers 
            if items[j]>items[j+1]:    # if the first number is greater than the second number swap them 
                temp = items[j]  # holding for the swap 
                items[j]= items[j+1]   # this is where the swap happens
                items[j+1] = temp  # second swap 

# items = [4,2,7,5,6,1]
# bubble_sort(items)
# print(items)
# is_sorted(items)
# print(is_sorted(items))

def selection_sort(items):  #2 nested loops 
    for i in range(5):  #using min to iterate through the list
        min = i   # holding variable for main position 
        for j in range(i,6):   #after every iteration we have to change the size of array
            if items[j] < items[min]:   #looking for the min value in this loop
                min = j   # comparing numbers and swapping 
        temp = items[i]     # changing min position when new min is found
        items[i] = items[min]
        items[min] = temp       #swap numbers





# items = [5,3,8,6,7,2]
# selection_sort(items)
# print(items)
# is_sorted(items)
# print(is_sorted(items))



def insertion_sort(items):  #
    for i in range(1, len(items)):   # iterating thorugh all unsorted items 
        j = i    # checking for swappable values when comparing through the array from the left 
        while items[j-1] > items[j] and j > 0:    # checking if values are swapple and inserting the number if it is 
            items[j-1], items[j] = items[j], items[j-1] # the actual code to swap 
            j-=1   #inserting into the list



items = [6,4,9,7,8,3]
insertion_sort(items)
print(items)
is_sorted(items)
print(is_sorted(items))
