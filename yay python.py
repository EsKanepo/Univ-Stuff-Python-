arr = [7, 1, 4, 8, 10, 3, 2]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
