def pangkat(x,y):
    if y == 0:
        hasil = 1
    elif y == 1:
        hasil = x
    else:
        hasil1 = pangkat(x,y//2)       #o log n
        if y % 2 == 0:
            hasil = hasil1*hasil1
        else:
            hasil = hasil1 * hasil1 * x
    print(f"x: {x**(y//2)} n/2 : {y//2}")
    return hasil

a, b = map(int, input().split())
hasil = pangkat(a,b)
print("Hasil akhir:", hasil)

#Tn : O(log n)
