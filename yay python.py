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

#No 3
def perkalian_matriks(m1, m2):
    baris1 = len(m1)
    baris2 = len(m2)
    kolom1 = len(m1[0])
    kolom2 = len(m2[0])
    hasil = [[0 for _ in range(kolom2)] for _ in range(baris1)]
 
    for i in range(baris1):
        for j in range(kolom2):
            for k in range(kolom1):
                hasil[i][j] += m1[i][k] * m2[k][j]
    return hasil
 
def data_matriks(baris, kolom):
    m = []
    for i in range(baris):
        baris_matriks = list(map(int, input().split()))
        m.append(baris_matriks)
    return m
 
 
N = int(input("Masukkan Untuk Kolom dan Baris : "))
 
print("Matriks 1 :")
m1 = data_matriks(N, N)
print("Matriks 2 :")
m2 = data_matriks(N, N)
 
hasil = perkalian_matriks(m1, m2)
for baris in hasil:
    print(baris)

Tn(max)= (O(1)*O(1)+O(1)+O(1)+O(1)+O(1)+(O(n)*O(n)*O(n))+O(1))+O(1)*O(1)+O(n)*O(1)+O(1)+O(1)+O(1)
Tn(max)= O(n^3)

