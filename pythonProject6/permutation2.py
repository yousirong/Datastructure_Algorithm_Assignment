def permutation(P, flag, i, n):
    if (i == n+1):
        for j in range(1,n+1):     # 순열 출력
            print(P[j], end = ' ')
        print()
#        print(P)
        return
    else:
        for j in range(1,n+1):
            if flag[j] == False:
                P[i] = j
                flag[j] = True
                permutation(P, flag, i+1, n)
                flag[j] = False

def main():
    n = int(input())
    P = [None]*(n+1)
    flag = [None]*(n+1)
    for i in range(1, n+1):
        flag[i] = False

    permutation(P, flag, 1, n)

if __name__ == '__main__':
    main()
