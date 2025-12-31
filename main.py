def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps happened, array is already sorted
        if not swapped:
            return


if __name__ == "__main__":
    arr = [1, 52, 5, 3, 53, 6, 5]
    bubbleSort(arr)
    print(arr)
