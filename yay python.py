n = list(map(int,input("Masukkan angka : ").split()))

hitung = [0] * 10
for i in n:
    hitung[i] += 1

for c in hitung:
    print(c)

Tn(max) = O(1)+O(1)+(O(n)*O(1))+(O(n)*O(1))
Tn(max) = O(1),O(1),O(n),O(n)
Tn(max) = O(n)
