def bubble_sort(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    if n - 1 != 0:
        bubble_sort(arr, n - 1)

    return arr

if __name__ == '__main__':
    arr = []
    length = int(input("Masukkan panjang array : "))
    
    for i in range(length):
        _ele = int(input("Masukkan nilai : "))
        arr.append(_ele)
    
    print(bubble_sort(arr, len(arr)))
