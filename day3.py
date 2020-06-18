# i = 1
# for i in range(5):
#     print('*'*i)
#
# # 方法二
# for i in range(4):
#     for j in range(i+1):
#         print("*", end='')
#     print()

# 九九乘法口诀
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d * %d = %2d  ' %(i, j, i * j), end='')
    print('')


