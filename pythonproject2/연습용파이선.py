#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210313
# 2-2) 4지 선다형 문항들의 정답과 문항별 배점이 주어질 때, 제출한 n개의 답안지를 채점하여 최저 성적과 최고 성적을 출력하시오
# 입력 예
# 2 4 1 3 3 2  # 문항별 정답
# 3 3 3 3 4 4  # 문항별 배점
# 4             # 체출한 답안지 수 n
# 3 3 3 3 3 3  # 제출한 답안지1
# 2 2 2 2 2 2  # 제출한 답안지2
# 4 4 4 4 4 4  # 제출한 답안지3
# 2 4 1 3 3 2  # 제출한 답안지4
#
# 출력 예
# 3 20

class Stu:
    minmaxli = []
    count = 6          # 6문항
    def inputs(ans):
        Stu.ans = ans
        while True:
            Stu.dap = str(Stu.ans)
            if len(Stu.dap) == Stu.count:
                break

    def points(poi):
        Stu.poi = poi
        while True:
            Stu.point = Stu.poi
            if len(Stu.point) == Stu.count:
                Stu.spoint = list(Stu.point)  # re.findall("\d", Stu.point)
                Stu.totscore = sum(map(int, Stu.spoint))
                break


    def __init__(self, num):
        self.tot = 0
        self.num = num
        print(self.num, '.', end='')
        self.name = ''
        while True:
            print(self.name, end='')
            self.dap = input('답안을 입력해주세요.(' + str(Stu.count) + '개) ')
            if len(self.dap) == Stu.count:
                break

    def calc(self):
#        print(self.num, end=' ')
#        print(self.name, end=' ')
        for j in range(Stu.count):
            if Stu.dap[j] == self.dap[j]:
                self.tot = self.tot + int(Stu.spoint[j]) # self.tot = self.tot + ((Stu.count / Stu.totscore)*100)
#               print('o', end='')

#            else:
#                print('x', end='')
        Stu.minmaxli += [int(self.tot)]
#        print(self.tot)
#        print(Stu.minmaxli)


    # 정답입력
s =int(input())
Stu.inputs(s)
r =input()
Stu.points(r)
# 답안입력

count = int(input())
li = []
for i in range(count):
    li.append(Stu(i + 1))

minmaxli = []
for i in li:
    i.calc()

print(min(Stu.minmaxli), max(Stu.minmaxli))
