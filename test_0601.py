# _*_ coding: utf-8 _*_
import random


# a = random.randint(1, 100)
# i = 0
# while i < 100:
#     b = int(input('please a number: '))
#     if isinstance(b, int):
#         print('输入值已转为Int')
#     if a == b:
#         print('找到相等的值')
#         break
#     if a < b:
#         print('输入值太大了')
#         i = i + 1
#     else:
#         print('输入值太小了')
#         i= i + 1

def multiplication(a, b, c):
    return a * b * c


if __name__ == '__main__':
    a = int(input('输入第一个数：'))
    b = int(input('输入第二个数：'))
    c = int(input('输入第三个数：'))
    mul = multiplication(a, b, c)
    print(f'三个数的乘积为{mul}')

