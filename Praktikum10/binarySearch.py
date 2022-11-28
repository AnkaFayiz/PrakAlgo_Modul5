def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

if __name__ == '__main__':
    arr = []
    n = int(input("Masukkan nilai n : "))

    for i in range(n):
        _element = int(input("Masukkan element : "))
        arr.append(_element)
    goals = int(input("Masukkan elemen yang dicari : "))
    result = binarySearch(arr, 0, len(arr) - 1, goals)
    print(arr)

    if result != -1:
        print("Element ditemukan di index ke-", str(result)) 
    else:
        print("Element tidak ditemukan di dalam index list!")
