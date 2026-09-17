def bubble_sort_inverted(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
                
        if not swapped:
            break
    return arr


numeros = [64, 1, 25, 16, 2, 72, 100]
print(bubble_sort_inverted(numeros))