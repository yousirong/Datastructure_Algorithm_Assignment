# 2-3) 가장 위의 행의 어떤 셀로부터 왼쪽 아래 대각선 방향 혹은 아래쪽 방향
# 혹은 오른쪽 아래 대각선 방향으로만 가면서 가장 아래 행의 어떤 셀까지
# 가는 경로의 최소비용을 구하는 프로그램을 동적계획법을 이용하여 작성하시오.
# 경로의 비용이란 지나가는 셀의 비용의 총합이다.

def mngrid_solution(m, n):
    AA_mn = [0] * n  # 1행부터 마지막행 까지의 경로의 최소비용 총합 배열
    AA_result = [0] * n  # AA_mn으로 부터 최소비용값 copy()값
    row = [0] * m   # 입력받은 셀 비용 배열
    n_row = [0] * m # 새로운 입력받은 셀 비용 배열
    for i in range(m - 1, -1, -1):  # 입력받은 셀 비용값을 정리함
        row[i] = list(map(int, input().split()))
    for i in range(0, m):   # 입력받은 셀 비용값을 n_row배열에 옮김
        n_row[i] = row[m - i - 1]
    # base case
    for a in range(n):   # 부분문제 해결을 위한 테이블 1행 비용값 옮김
        AA_mn[a] = n_row[0][a]

    for i in range(1, m):
        if i == 1:    # 1행 일때
            for j in range(n):  # 열비용 검사 - > 오른쪽 왼쪽 아래쪽 방향 정하는 부분
                if n == 1:  # 1열 일경우 왼쪽열은 없음
                    AA_mn[j] = n_row[i - 1][j] + n_row[i][j]
                else:  # 1열이 아닌경우 오른쪽왼쪽아래쪽 선택 가능
                    if j == 0:  # 아래쪽 방향 선택시 부분문제
                        AA_mn[j] = min(n_row[i - 1][j], n_row[i - 1][j + 1])+n_row[i][j]
                    elif j == n - 1:   # 왼쪽 방향 선택시 부분 문제
                        AA_mn[j] = min(n_row[i - 1][j - 1], n_row[i - 1][j]) +n_row[i][j]
                    else:   # 오른쪽 방향 선택시 부분 문제
                        AA_mn[j] = min(n_row[i - 1][j],n_row[i - 1][j - 1], n_row[i - 1][j + 1])+n_row[i][j]
            AA_result = AA_mn.copy()   # 구한 최소비용 배열을 새로운 배열에 저장
        elif i >= 2:  # 2행 이상일 때
            for j in range(n):  # 열비용 검사 - > 오른쪽 왼쪽 아래쪽 방향 정하는 부분
                if n == 1:
                    AA_mn[j] = n_row[i][j] + AA_result[j]  # 1열 일경우 왼쪽열은 없음
                else:  # 1열이 아닌경우 오른쪽왼쪽아래쪽 선택 가능
                    if j == 0:  # 아래쪽 방향 선택시 부분문제
                        AA_mn[j] = min(AA_result[j], AA_result[j + 1])+n_row[i][j]
                    elif j == n - 1:  # 왼쪽 방향 선택시 부분 문제
                        AA_mn[j] = min(AA_result[j - 1], AA_result[j])+n_row[i][j]
                    else:   # 오른쪽 방향 선택시 부분 문제
                        AA_mn[j] = min(AA_result[j - 1], AA_result[j], AA_result[j + 1])+ n_row[i][j]
            AA_result = AA_mn.copy()    # 구한 최소비용 배열을 새로운 배열에 저장
    print(min(AA_mn))   # 모든 최소 비용값중에 최소값 출력

m, n = map(int, input().split())  # m*n격자 행과 열 값 입력
mngrid_solution(m, n)
'''
4 5   
2 8 9 5 8
4 9 6 5 3
6 7 5 2 1
3 2 5 4 8
'''