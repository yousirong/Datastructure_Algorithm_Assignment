#              1.제목:한국외대 알고리즘 과제
#              2.날짜:20210929
# 문제 1-3
#3) n개의 수(109이하 –109이상 정수)들과 d(0이상 정수)가 주어져 있다.
# 이들 n개의 수 중에서 다음 조건을 만족하는 수들을 선택하려고 한다: 조건)
# 모든 두 수의 차이가 d이하이다. 이렇게 선택할 수 있는 수들의 최대 개수를 구하는
# 프로그램을 작성하시오.
#제약 조건:
#(i) 정렬을 이용한다.
#(ii) 정렬 알고리즘은 퀵 정렬을 사용하고, 피봇은 random하게 선택한다.
from math import dist
n = int(input())  # n
n_list = list(map(int, input().split()))  # n 개의 정수
d = int(input())

def quick_sort(A):  # 퀵 정렬 알고리즘
    if(len(A)>1):   # 정렬할때 받아오는 list에 적어도 한개의 원소가 있어야함.
        import random    # random함수 import
        pivot = A[random.randint(0, len(A)-1)]  # random.randint 균일분포의 정수 난수 1개 생성
        greater = [i for i in A if i > pivot]  # pivot보다 큰 값
        smaller = [i for i in A if i < pivot]  # pivot보다 작은 값
        middle = [i for i in A if i == pivot]  # pivot과 동일한 값
        return quick_sort(smaller) + middle + quick_sort(greater)  # 다시 크기 순으로 리스트 합
    else:
        return A   # list의 원소가 없을 경우 반환

def solution(n, n_list, d):
    new_n_list = quick_sort(n_list)  # n_list을 quicksort함
    x = 0
    result = 0 # 결과값 출력
    for i in range(0, n):   # 입력 받은 n개 만큼 for 구문
        if abs(new_n_list[x] - new_n_list[i]) <=d:   # [x] 와 [i]의 차이의 절대 값이 0보다 작을경우
            result = len(new_n_list[x:i+1])  # result 변수에 길이 저장
        else:
            x+=1    # 두 수의 차이가 d보다 클 경우
    print(result)   # 결과 출력

solution(n, n_list, d)
'''
6
3 10 50 15 25 14
5
'''
