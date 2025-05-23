def matriks(N, dimesi, Q):
    dp = []
    countopt = []
    countall = []
    for x in range(N):
        dp.append([0] * N)
        countopt.append([0] * N)
        countall.append([0] * N)
    for i in range(N):
            countopt[i][i] = 1
            countall[i][i] = 1
    for panjang in range(2, N + 1):
        for i in range(N - panjang + 1):
            j = i + panjang - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensi[i] * dimensi[k+1] * dimensi[j+1]
                totalall = (countall[i][k] * countall[k+1][j]) % 26101991
                countall[i][j] = (countall[i][j] + totalall) % 26101991
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    countopt[i][j] = (countopt[i][k] * countopt[k+1][j]) % 26101991
                elif cost == dp[i][j]:  
                    countopt[i][j] = (countopt[i][j] + (countopt[i][k] * countopt[k+1][j]) % 26101991) % 26101991
    if Q == 1:
        return dp[0][N - 1]
    elif Q == 2:
        return countopt[0][N - 1]
    elif Q == 3:
        return countll[0][N - 1]
    
N = int(input())
dimensi = list(map(int, input().split()))
Q = int(input())
print(matriks(N, dimensi, Q))
