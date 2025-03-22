#No 1
n = list(map(int,input("Masukkan angka : ").split()))

hitung = [0] * 10
for i in n:
    hitung[i] += 1

for c in hitung:
    print(c)

Tn(max) = O(1)+O(1)+(O(n)*O(1))+(O(n)*O(1))
Tn(max) = O(1),O(1),O(n),O(n)
Tn(max) = O(n)

#No 2
text = input("Masukkan teks : ").split()
huruf = []

for i in range(len(text)):
    for j in range(len(text[i])):
        huruf.append(text[i][j])

for i in range(len(huruf)):
    for j in range(len(huruf)-i-1):
        if ord(huruf[j]) > ord(huruf[j+1]):
            huruf[j],huruf[j+1] = huruf[j+1] , huruf[j]

print(" ".join(huruf))

Tn(max) = O(1)+O(1)+(O(n)*O(n)*O(1))+(O(n)*O(n)*O(1)*O(1))+O(1)
Tn(max) = O(1),O(1),O(n^2),O(n^2),O(1)
Tn(max) = O(n^2)
