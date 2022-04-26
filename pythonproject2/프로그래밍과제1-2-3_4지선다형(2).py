#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210317
# 2-3) 4지 선다형 문항들의 정답과 문항별 배점이 주어질 때, 제출한 n개의 답안지를 채점하여 (2)
# 정답률이 가장 낮은 문제의 번호를 출력하시오.
# 정답률이 가장 낮은 문제 여러 개일 경우 이 문제들의 번호를 오름차순으로 출력하시오.
#
# 입력 예
# 2 4 1 3 3 2  # 문항별 정답
# 3 3 3 3 4 4  # 문항별 배점
# 4             # 체출한 답안지 수 n
# 3 3 1 3 3 3  # 제출한 답안지1
# 2 2 2 2 2 2  # 제출한 답안지2
# 4 4 4 4 4 4  # 제출한 답안지3
# 1 1 1 1 1 1  # 제출한 답안지4
#
# 출력 예
# 1 2 4 5 6
import _operator
import re
class Stu:
    res_sublist = list()
    totlist = list()
    ascentotlist = list()
    def inputs(self):  # 문제 정답 답안 입력(숫자 상관 x)
        Stu.count = len(self)  # 정답의 개수에 따라 count변수에 stirng 길이 만큼 초기화
        Stu.sinput = list(self)  # 문제별 정답을 리스트로 변환하여 sinput변수에 초기화
        for i in range(1, Stu.count + 1, 1):
            Stu.res_sublist.append(1)       # 오름차순 정렬해주는 함수의 보조 리스트
        for t in range(1, Stu.count + 1, 1):
            Stu.totlist.append(0)          # 정답 개수 리스트
        for x in range(1, Stu.count + 1, 1):
            Stu.ascentotlist.append(x)     # 정답률 오름차순 문제 번호 매기기용
        return Stu.count, Stu.sinput # count, sinput변수 리턴

    def points(self):  # 문제별 베점 입력(숫자 상관 x)
        Stu.spoint = list(self)  # 문제별 배점 string으로 받아서 list로 변환하여 spoint에 초기화
        while True:
            if len(Stu.spoint) == Stu.count:  # 문제별 배점 수와 정답의 개수가 같으면 함수 실행
                Stu.totscore = sum(map(int, Stu.spoint))  # 만약 개수가 같을 경우 문제의 총점 계산
                break
        return Stu.spoint, Stu.totscore  # 문제별 배점과 총점 리턴

    def __init__(self, num):   # __init__메서드는 학생수를 받으면 제출한 답안지를 받고 정답의 개수를 만족하면 n명의 배열 생성
        self.num = num  # 학생수
        self.tot = 0  # self.tot는 맞힌 문제 총점, 0으로 초기화
        self.dap = input()  # self.dap변수에 제출한 답안지 받기
        while True:
            if len(self.dap) == Stu.count:  # 제출한 학생들의 답안지가 답의 개수와 같을때
                self.sdap = list(self.dap)  # string으로 받은 답안지를 리스트로 변환 sdap에 초기화
                break

    def calc(self):
        Stu.ascenli1 = []  # ascenli1리스트를 루프 돌때마다 초기화 시키기
        for j in range(Stu.count):
            if Stu.sinput[j] == self.sdap[j]  :  # 인데스의 값이 같으면
                Stu.ascenli1 += [int(1)]  # 문제 맞으면 +1
            else:
                Stu.ascenli1 += [int(0)]  # 문제 틀리면 +0
                # for 구문 다 돌면 문제 개수 만큼의 맞힌 문제개수 리스트 형성
        Stu.totlist = [x + y for x, y in zip(Stu.totlist, Stu.ascenli1)]  # 전역변수리스트와 학생 맞힌 문제 개수 리스트
                                                                          # 같은 자리(index) 값을 합한다.

    def acending():    # 오름차순 Ascending 함수
        raterank = dict(zip(Stu.ascentotlist, Stu.totlist))   # key 문제번호(Stu.ascentotlist)
                                                              # value 정답개수
        res_list = [i for i, value in enumerate(raterank.values()) if value == min(raterank.values())]
        # 정답 개수가 최소일때 enumerate함수를 써서 열거하고
        res_list = [x+y for x,y in zip(res_list, Stu.res_sublist)] # value의 맞게 오름차순 정렬
        print(str(res_list))
# 정답입력
s = input()
Stu.inputs(s)
# 배점입력
p = input()
Stu.points(p)
# 답안입력

count = int(input())  # 제출한 답안지의 학생수를 받음
li = []  # 제출한 답안지의 학생 수에 따라 li리스트 변수에 학생수 만큼 리스트 생성
for y in range(count):
    li.append(Stu(y + 1))

for z in li:  # 학생수 만큼 calc 함수 돌려서 총점 확인
    z.calc()

Stu.acending()  # 오름차순으로 정렬해주는 함수 실행

# goorm과제 제출 시스템에서 요구하는 입력값과 출력값을 정확히 처리하기 위해 확인을 위한 중간에 변수
# 확인을 위한 print함수는 다 제거 했습니다.
# 2-1번과 2-2번과 같이 runtime error를 잡지 못했습니다.