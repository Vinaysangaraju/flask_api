def bubble(arr):
    lens = len(arr)
    for i in range(lens-1):
        for j in range(lens - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return print(arr)

bubble([20,10,50,60,40])