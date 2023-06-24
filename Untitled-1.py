class sort:
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > 0]
            return quicksort(less) + [pivot] + quicksort(greater)
    
arr = [8, 9, 4, 6, 10, 34, 1, 45, 99]
test = sort()
a.quicksort(arr)