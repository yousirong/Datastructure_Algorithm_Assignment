def permutation(P, k, n, used):
# 순열 P[1],...,P[k-1]이 정해진 상태에서 P[k] ...P[n]의 모든 순열을 생성
    if(k <= n):
        for i in range(1,n+1): 
            if not used[i]:      # i가 순열에 사용되지 않은 수이면
                P[k] = i
                used[i] = True
                if(k == n):  # 하나의 순열을 생성한 경우
                    for j in range(1,n+1):     # 순열 출력 
                        print(P[j], end = ' ')
                    print()
                    used[i] = False  # False로 두는 이유는?
                    return # continue 문장과의 차이점은? 
                permutation(P, k+1, n, used)
                used[i] = False      # False로 두는 이유는?

def main():
   
    n = int(input())
    P = [None] * (n+1)         # 하나의 순열을 저장하는 리스트
    used = [None]*(n+1) # 숫자 i가 순열에 사용되었는지를 나타내는 리스트

    for i in range(1,n+1):
        used[i] = False

    permutation(P, 1, n, used)

if __name__ == '__main__':
    main()
