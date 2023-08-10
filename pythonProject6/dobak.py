import random
# 복권
i = random.randint(1, 100)
print(i)
random.seed(i)
for i in range(5):
    print(sorted(random.sample(range(1, 46), 6)))


# 연금복권
print("Groups", random.sample(range(1, 6), 1))
print("Number", [random.randint(0, 9) for i in range(6)])

# 연금복권2
# num = [7,8,12,13,15,26,27,28,30,31,35,38]
# print(sorted(random.sample(num, 6)))
