#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210317
# 2-1) 4지 선다형 문제들의 정답과 문제별 배점이 주어질 때, 제출한 답안지의 점수를 계산하는 프로그램을 작성하시오.

# 입력 예:
# 2 4 1 3 3 2  # 문제별 정답 (1번 문제 정답: 2, 2번 문제 정답: 4, ..., 6번 문제 정답 2)
# 3 3 3 3 4 4  # 문제별 배점 (1번 문제 점수: 3, 2번 문제 점수: 3, ..., 6번 문제 점수 4)
# 1 4 3 4 1 2  # 제출한 답안지 (1번 문제: 1, 2번 문제: 4, ..., 6번 문제: 2)

# 출력 예
# 7   # 정답을 맞춘 문제: 2번, 6번
# -*- coding: utf-8 -*-

class Stu:
    def inputs(self):  # 문제 정답 답안 입력(숫자 상관 x)
        Stu.count = len(self)     # 정답의 개수에 따라 count변수에 stirng 길이 만큼 초기화
        Stu.sinput = list(self)   # 문제별 정답을 리스트로 변환하여 sinput변수에 초기화
        return Stu.count, Stu.sinput    # count, sinput변수 리턴

    def points(self):  # 문제별 베점 입력(숫자 상관 x)
        Stu.spoint = list(self)   # 문제별 배점 string으로 받아서 list로 변환하여 spoint에 초기화
        return Stu.spoint         # spoint변수 리턴

    def __init__(self, num):  # __init__메서드는 학생수를 받으면 제출한 답안지를 받고 정답의 개수를 만족하면 n명의 배열 생성
        self.num = num        # 학생수
        self.tot = 0          # self.tot는 맞힌 문제 총점, 0으로 초기화
        self.dap = input()         # self.dap변수에 제출한 답안지 받기
        self.sdap = list(self.dap)  # string으로 받은 답안지를 리스트로 변환 sdap에 초기화

    def calc(self):  # calc 함수는 정답과 답안지의 값이 같으면 self.tot(총점)변수에 배점을 더하는 함수
        for j in range(len(Stu.sinput)):    # 정답수 만큼의 길이로 for구문 돌려서 Stu.input(답안지)와 self.dap(학생답안지)
            if self.dap[j] == Stu.sinput[j]:     # 인데스의 값이 같으면
                self.tot = self.tot + int(Stu.spoint[j])  # 해당하는 문제의 배점을 총점에 더해나감
        print(self.tot)
# 정답입력
s = input()
Stu.inputs(s)    # 함수 inputs 호출
# 배점입력
p = input()
Stu.points(p)    # 함수 points 호출
# 답안입력
count = 1        # 2-1 문제에서 정답의 개수와 상관없이 학생수는 1명이므로 1로 초기화
li = []        # 제출한 답안지의 학생 수에 따라 li리스트 변수에 학생수 만큼 리스트 생성
for z in range(count):
    li.append(Stu(z + 1))
for p in li:   # 학생수 만큼 calc 함수 돌려서 총점 확인
    p.calc()
# goorm과제 제출 시스템에서 요구하는 입력값과 출력값을 정확히 처리하기 위해 확인을 위한 중간에 변수
# 확인을 위한 print함수는 다 제거 했습니다.
# runtime error를 잡지 못했습니다.
