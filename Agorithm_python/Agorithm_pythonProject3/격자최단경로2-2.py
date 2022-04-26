# 2-2) 셀 (1,1)에서 오른쪽 방향 혹은 아래쪽 방향으로만 가면서 셀 까지 가는 경로의 최소비용을
# 구하는 프로그램을 동적계획법을 이용하여 작성하시오. 경로의 비용이란 지나가는 셀의 비용의 총합이다.
# 단, 특정 셀 (p,q)를 반드시 지나가야 한다.

# 입력: 위의 입력 마지막 줄에 p q가 주어진다. 단, (p,q)는 (1,1)과 (m,n)은 아니다.
def mngrid_solution(m, n):
    if 1<= m and n<= 2000:
        AA_pq = [0] * n  # (1,1)부터 (p,q)까지의 경로의 최소비용 총합 배열
        pq_mn = [0] * n  # (p,q)부터 (m,n)까지의 경로의 최소 비용 총합 배열
        A_copy = [0] * n  # AA_pq에서 copy()을 이용해서 부분문제의 해의 값을 저장하는 테이블
        B_copy = [0] * n  # pq_mn에서 copy()을 이용해서 부분문제의 해의 값을 저장하는 테이블
        row = [0] * m  # 입력 받은 셀 비용 배열
        n_row = [0] * m  # 새로운 입력받은 셀 비용 배열
        for i in range(m - 1, -1, -1):  # 입력받은 셀 비용값을 정리함
            row[i] = list(map(int, input().split()))  # 입력된 행기준으로 배열에 대입
        for i in range(0, m):
            n_row[i] = row[m - i - 1]
        p, q = map(int, input().split())  # p,q 입력 받기

        for a in range(q):  # 부분문제의 해의 값 저장하는 테이블
            if a == 0:
                AA_pq[a] = n_row[0][a]  # 1행 밑에 0행의 부분문제를 구하기 위한 배열 생성
            else:
                AA_pq[a] = AA_pq[a - 1] + n_row[0][a]
            A_copy = AA_pq.copy()
        for i in range(1, p):  # (1,1)에서 (p,q)까지 최소비용 구함
            for j in range(q):   # 문제에서 p,q 좌표가 1,1 m,n일 경우는 없다고 했으므로 q=1일 경우는 생략합니다.
                if j == 0:   # 0열 일 경우
                    AA_pq[j] = AA_pq[j] + n_row[i][j]
                else:   # 0열이 아닐경우
                    AA_pq[j] = n_row[i][j] + min(AA_pq[j - 1], A_copy[j])  # 점화식
                A_copy = AA_pq.copy()
        n_row[p - 1][q - 1] = AA_pq[q - 1]  # (p,q)에 방금 구한 최소비용 대입
        for a in range(q - 1, n):  # (p,q)에서 (m,n)까지 구하기 위한 부분문제의 해의 값을 저장하는 테이블
            if a == q - 1:
                pq_mn[a] = n_row[p - 1][a]
            else:
                pq_mn[a] = pq_mn[a - 1] + n_row[p - 1][a]
            B_copy = pq_mn.copy()
        for i in range(p, m):  # (p,q)에서 (m,n)까지 최소비용 구함
            for j in range(q - 1, n): # 문제에서 p,q 좌표가 1,1 m,n일 경우는 없다고 했으므로 j=q일 경우는 생략합니다.
                if j == q - 1:  # 비용계산하는 첫 열일 경우
                    pq_mn[j] = pq_mn[j] + n_row[i][j]
                else:      # 첫 열이 아닐 경우
                    pq_mn[j] = n_row[i][j] + min(pq_mn[j - 1], B_copy[j])
                B_copy = pq_mn.copy()
        print(pq_mn[-1])  # 부분 문제의 테이블 배열에서 제일 마지막 최소비용을 출력

m, n = map(int, input().split())  # m*n격자 테이블 행과 열값 입력
mngrid_solution(m, n)
'''
4 5   
2 8 9 5 8
4 9 6 5 3
6 7 5 2 1
3 2 5 4 8
2 3
'''