#1-2) n(1이상 10,000이하 정수)개 계단을 바닥에서 위로 올라가려고 한다.
# 계단을 올라갈 때 한 번에 s개 이하의 계단만 오를 수 있으며,
# 각 계단은 밟을 때 비용이 있다.
# 바닥에서 가장 위의 계단으로 올라갈 때 밟는 계단의 비용 합이 최소가 되도록 하면서 올라가고자 한다.
# 이때의 비용합(최소 비용)을 구하는 프로그램을 작성하시오.
def min_costs_step(n, s_stair, cost):
    if 1 <= n <= 10000:
        cost.insert(0, 0)  # 0번째 계단 비용를 추가함
        arr = [100000000000 for i in range(n+1)]  # 0부터 n까지 큰 수 를 담은 arr배열
        # n번째 계단까지 최소비용을 출력하는 배열을 만듦
        arr[0] = 0  # 0번째 계단은 비용이 0임
        s_li=list((range(1, s_stair+1)))  # s개 이하의 계단오르는 값을 배열에 저장
        for i in range(n+1):  # 1-2문제에서는 s개 이하의 계단만 오른다고 했으므로 몇개 오로는지 입력받아야 알 수 있음
            for k in s_li:   # s_li배열의 값들을 하나씩 검사
                if i >=k:  # arr배열에 저장할 인덱스 값과 s개 계단을 하나씩 검사해서
                    arr[i] = min(arr[i], arr[i-k]+ cost[i]) # arr에 저장된 최소비용과 전 계단과 다음 밟을 계단의 비용을
                    # 더한 값중에 최소인 값을 i번째 arr배열에 갱신해 나아감.
                    # 계단 최소비용중에 최소값을 arr배열에 저장
                else:
                    break   # 위의 조건을 만족하지 않은면 break
        if arr[n] == 100000000000:   # 초기화된 큰 수가 계속 남아있다면 return -1
            return -1
        else:  # 정상적으로 최소비용이 출력될 경우
            return arr[n]
n, s_stair = list(map(int, input().split()))  # n개의 계단과 s개 이하의 계단을 오르는 값
cost = list(map(int, input().split()))   # 계단 오르는데 비용
print(min_costs_step(n, s_stair, cost))
'''
7 1
3 7 9 9 2 5 4
'''