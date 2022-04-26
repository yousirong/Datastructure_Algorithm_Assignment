#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210911
# 문제 1-1
# 1) 주식 투자를 즐기는 홍길동은 n일 동안 어떤 회사의 주식을 다음과 같이 매매한다: 주식 한 주를 한 번만 사서 이를 다음에 한 번 팔 수 있다.
# 홍길동은 n일 동안 주식 매매(한번 사서 한번 판다)를 하여 얻은 이익에 대하여, 얻을 수 있는 최대 이익과 얼마나 차이가 있는지를 알고 싶어한다.
# 그래서 이 기간 동안 얻을 수 있는 최대 이익을 계산하기로 하였다.
# 예를 들어, 7일 동안 주식 가격이 (30, 25, 50, 10, 20, 40)과 같을 때,
# 최대 이익은 네째 날 주식을 사서 마지막 날 팔면 이익이 30(=40–10)이다.
# n일 동안 주식 가격이 주어질 때, 얻을 수 있는 최대 이익을 구하는 프로그램을 작성하시오.

# 입력 예
# 첫째 줄에는 n이 주어진다. n은 2 이상 100,000 이하의 정수이다. 둘째 줄에는 주식 가격(양의 정수)이 날짜 순서대로 n개 주어진다.

# 출력 예
# 최대 이익을 첫 번째 줄에 출력한다. 두 번째 줄에 사는 가격과 파는 가격을 각각 출력한다.
# 최대 이익을 얻는 경우가 여러 개일 때는, 사는 가격이 최소인 경우 하나만 출력한다. 이득이 없는 경우는, –1만 출력한다.

a = int(input())
b = list()  # 후보 값 리스트
stock = list(map(int, input().split()))  # 주식 가격리스트

upperlimit_stock = stock[0]
upperlimit_index = 0
underlimit_stock = stock[0]
underlimit_index = 0

for i in range(1, len(stock)):
# for i in range(1, a):
    n = stock[i]
    if upperlimit_stock < n:  # n이 원래의 max값보다 클 경우에는 n을 max값으로 업데이트하고, 인덱스를 i로 업데이트함
        upperlimit_stock = n
        upperlimit_index = i
    elif underlimit_stock > n:  # n가 원래 min값보다 작을 경우엔 리스트에 기존 값을 담고 다시 돌린다.
        b.append((upperlimit_stock - underlimit_stock, upperlimit_stock, underlimit_stock))
        underlimit_stock = n
        underlimit_index = i
        upperlimit_stock = n
        upperlimit_index = i

b.append((upperlimit_stock - underlimit_stock, upperlimit_stock, underlimit_stock))
# for문이 끝나고 난 뒤의 최대 이익(price_max - price_min)과, 최대값과 최소값을 각각 넣는다.

price_sorted = sorted(b, key=lambda n: (-n[0], n[2]))
# list에 앞에서부터 이익이 큰 값을 넣고, 이익이 같은 경우 최소값이 낮은 것부터 넣는다.

if upperlimit_index <= underlimit_index:  # 최대값 인덱스가 더 작을 경우. 이럴 땐 최대 이익이 없으므로 -1 출력
    print(-1)
else:
    print(price_sorted[0][1] - price_sorted[0][2])
    print(price_sorted[0][2], price_sorted[0][1])
'''
15   -> 20?
15
6 5 10 5 7 9 25 1 4 10 6 23 5 3 12 2 4 24 14 10
'''
'''
입력받은 수를 그대로 for 구문 돌아서 최소값을 찾기 때문에 O(n)
'''
'''
10
20 19 18 17 16 10 9 8 7 6 
'''
