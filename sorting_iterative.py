#!python


def is_sorted(items):
    if len(items) in [0, 1]:
        return True
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True


def bubble_sort(items):
    for i in range(len(items)-1,0,-1):
        for j in range(i):
            if items[j]>items[j+1]:
                temp = items[j]
                items[j]= items[j+1]
                items[j+1] = temp

# items = [4,2,7,5,6,1]
# bubble_sort(items)
# print(items)
# is_sorted(items)
# print(is_sorted(items))

def selection_sort(items):
    for i in range(5):
        min = i
        for j in range(i,6):
            if items[j] < items[min]:
                min = j
        temp = items[i]
        items[i] = items[min]
        items[min] = temp





# items = [5,3,8,6,7,2]
# selection_sort(items)
# print(items)
# is_sorted(items)
# print(is_sorted(items))



def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while items[j-1] > items[j] and j > 0:
            items[j-1], items[j] = items[j], items[j-1]
            j-=1 



items = [6,4,9,7,8,3]
insertion_sort(items)
print(items)
is_sorted(items)
print(is_sorted(items))
