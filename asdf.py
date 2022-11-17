import sys

# print(sys.argv[1])
#
# input_list = sys.argv[1].split(",")
# result = 0
# for i in input_list:
#     result += int(i)
# print(result)

# result = sum([int(i) for i in sys.argv[1].split(",")])
result = sum(map(int, sys.argv[1].split(",")))
print(result)

# print(f"{sys.argv[1]}를 받은 인수입니다.{sys.argv[0]}입니다.")