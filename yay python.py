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

#No 2
def cari(pattern, text):
    if pattern in text:
        return "Ketemu"
    return "Tidak Ketemu"
pattern_input = str(input("Pattern : ")).lower()
text_input = str(input("Text : ")).lower()
print(cari(pattern_input, text_input))

Tn(max) : O(1)+O(1)+O(1)+O(1)
Tn(max) : O(1),O(1),O(1),O(1)
Tn(max) : O(1)

#No 3
##def prime(n):
##    if n<2:
##        return False
##    for i in range(2, int(n**0.5)+1):
##        if n % i == 0:
##            return False
##    else:
##        return True
## 
##angka = list(map(int,input('Masukkan bilangan acak : ').split()))
##x = 0
##for i in angka :
##    if prime(i):
##        x += 1
##print(x)
##
##Tn(max) : O(n)+O(1)+O(1)+O(1)
##Tn(max) : O(n),O(1),O(1),O(1)
##Tn(max) : O(n)
