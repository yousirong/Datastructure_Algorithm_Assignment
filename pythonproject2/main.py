#              1.제목:한국외대 자료 구조 과제
#              2.날짜:20210312
# 2-1) 4지 선다형 문제들의 정답과 문제별 배점이 주어질 때, 제출한 답안지의 점수를 계산하는 프로그램을 작성하시오.

# 입력 예:
# 2 4 1 3 3 2  # 문제별 정답 (1번 문제 정답: 2, 2번 문제 정답: 4, ..., 6번 문제 정답 2) 241332333344143412
# 3 3 3 3 4 4  # 문제별 배점 (1번 문제 점수: 3, 2번 문제 점수: 3, ..., 6번 문제 점수 4)
# 1 4 3 4 1 2  # 제출한 답안지 (1번 문제: 1, 2번 문제: 4, ..., 6번 문제: 2)

# 출력 예
# 7   # 정답을 맞춘 문제: 2번, 6번


a = [1, 2, 3, 4, 5]
print(len(a))
#
#
# class Stu:
#     count = 6
#     dap = ""
#     spoint = None
#     num = 0
#
#     def main__init__(self, num):
#         self.num = num
#         self.tot = 0
#         while True:
#             self.dap = input()
#             if len(self.dap) == Stu.count:
#                 print('')
#                 break
#
#     def calc(self):
#         self.count = count
#         for j in range(Stu.count):
#             if Stu.dap[j] == self.dap[j]:
#                 self.tot = self.tot + (int(Stu.spoint[j]))
#             else:
#                 print('', end='')
#         print(self.tot)
#     # 정답입력
#
#
# # Stu.inputs()
# # Stu.points()
# Stu.dap = input()
# while True:
#     if len(Stu.dap) == Stu.count:
#         break
# Stu.point = input()
# while True:
#     if len(Stu.point) == Stu.count:
#         Stu.spoint = re.findall("\d", Stu.point)
#         Stu.totscore = sum(map(int, Stu.spoint))
#         break
# # 답안입력
# count = 1
# li = []
# for i in range(count):
#     li.append(Stu(i + 1))
# for i in li:
#     i.calc()
