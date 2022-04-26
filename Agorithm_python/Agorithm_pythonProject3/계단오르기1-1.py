# 1-1) n(1 이상 10,000 이하 정수)개 계단을 바닥에서 위로 올라가려고 한다.
# 계단을 올라갈 때 한 번에 1개, 2개의 계단만 오를 수 있으며, 각 계단은 밟을 때 비용이 있다.
# 바닥에서 가장 위의 계단으로 올라갈 때 밟는 계단의 비용 합이 최소가 되도록 하면서 올라가고자 한다.
# 이때의 비용합(최소 비용)을 구하는 프로그램을 작성하시오.
import sys

def min_cost_step(n, cost):
    if 1 <= n <= 10000:
        cost.insert(0, 0)  # 0번째 계단 비용
        arr = [0 for i in range(n+1)]  # arr에는 최소값이 들어감
        arr[0], arr[1], arr[2] = cost[0], cost[1], cost[2]
        # 4번째까지는 최소값 구함
        for i in range(3, n+1):  # 3번째부터 n까지 for문을 돌림.
            arr[i] = min(arr[i-1], arr[i-2]) + cost[i]
        return arr[n]  # n번째 계단 비용의 최소값을 리턴

n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
print(min_cost_step(n, price))
'''
7
2 6 2 4 11 10 2
'''