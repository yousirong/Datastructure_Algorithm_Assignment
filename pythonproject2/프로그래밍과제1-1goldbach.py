#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210312
# 문제 1-1
# 2보다 큰 모든 짝수는 두 개의 소수(prime number)의 합으로 나타낼 수 있다는 Goldbach의 추측이 있다.
# 예를 들어 10 = 3 + 7, 20 = 7 + 13으로 나타낼 수 있다.
# 2보다 큰 임의의 짝수를 입력하여 이 짝수를 두 소수의 합으로 표현할 수 있는지를 결정하고
# 만약 표현할 수 있으면 차이가 가장 작은 두 소수의 합으로 나타내시오. 예를 들어 10 = 3 + 7 = 5 + 5이다.
# 문제에서 요구하는 결과는 5 + 5이다.
# 단, n이 소수인지 판별하는 함수를 정의하고 이를 사용하여야 함

# 입력 예
# 10  // 2000이하 정수

# 출력 예
# 5 5

# n이하의 숫자들 중 소수 찾기
def Find_pnbn(n):   # Find prime numbers below n 줄임말 --- 에라토스테네스의 체
    # 에라토스테네스의 체 초기화: n개의 요소에 True 설정 (소수로 간주)
    era = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if era[i] == True:                # i가 소수인 경우
            for j in range(i+i, n, i):     # i이후 i의 배수들을 False 판정
                era[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n) if era[i] == True]

# n 이하의 소수들 중 합이 n
# Sum_opnin 함수 설명: n 이하의 소수들 중 합이 n 이어야 하며 그 차이가 가장 작은 것을 return
# 찾은 소수들 중 max(n/2보다 작은 수)부터 합이 n이 되는 수를 찾는다.
def Sum_opnin(n):
    # Sum of prime numbers is n 줄임말
    sosu = Find_pnbn(n)                      # n 이하의 숫자들 중 소수 찾기 함수에서 소수 받아오기
    sosulen = max([i for i in range(len(sosu)) if sosu[i] <= n/2])   # 변수 sosulen에 최대 값의 길이를  반환함
    for i in range(sosulen, -1, -1):                             # 길이만큼 for구문을 두개를 써서 하나는 순방향
        for j in range(i, len(sosu)):                            # 다른 하나는 역방향으로 돌려서
            if sosu[i]+sosu[j] == n:                             # n 이하의 소수들 중 합이 n
                return [sosu[i], sosu[j]]                        # 합이 n 이면 리턴

n = int(input())
print(" ".join(map(str, Sum_opnin(n))))


