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

