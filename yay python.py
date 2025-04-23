#No 1
##n = input("Masukkan 8 koin : ")
##koin = list(n)
##idx = 1
##
##i = ord(koin[0])
##if koin[0] == koin[1]:
##    for i in range(2,8):
##        if koin[i]!= koin[0]:
##            idx = i+1
##            break
##elif koin[0] == koin[2]:
##    idx = 2
##
##else:
##    idx = 1
##
##print(idx)
##
##Tn(max) : O(1)+O(1)+O(1)+O(1)+O(1)*(O(n)+O(1)*(O(1)+O(1)))+O(1)*O(1)+O(1)*O(1)+O(1)
##Tn(max) : O(1),O(n),O(1),O(1)
##Tn(max) : O(n)

##def jumlah_genap(arr):
##    if len(arr) == 0:
##        return 0
##    elif len(arr) == 1:
##        if arr[0] % 2 == 0:
##            return arr[0]
##        else:
##            return 0
##    else:
##        mid = len(arr)//2
##        left = jumlah_genap(arr[:mid])
##        right = jumlah_genap(arr[mid:])
##        return left + right
##arr = [5, 2, 7, 8, 6, 3, 4]
##print(jumlah_genap(arr))
