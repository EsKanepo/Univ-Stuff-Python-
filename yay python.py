##arr = [7, 1, 4, 8, 10, 3, 2]  
##maks = arr[0]
##
##for i in arr:
##    if i > maks:
##        maks = i
##
##print("Bilangan terbesar adalah", maks)
##
##Tn(max) = O(1)+O(1)+(O(n)*O(1)*O(1))+O(1)
##Tn(max) = O(1),O(1),O(n),O(1)
##Tn(max) = O(n)

arr = [7, 1, 4, 8, 10, 3, 2]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

##Tn(max) =(O(1), O(n^2), O(1), O(1))
##Tn(max)= O(n^2)

