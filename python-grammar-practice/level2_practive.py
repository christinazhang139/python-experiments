# level2_practice.py
# -----------------------------
# 练习 5：打印 1~10 所有偶数
print("练习5: 打印1～10所有偶数")
for i in range(1,11):
    if i % 2 == 0:
        print(i)

print("\n-----------------------------")

# -----------------------------
# 练习 6：判断一个数字是否是奇数
# -----------------------------
print("练习 6：判断一个数字是否是奇数")

def is_odd(num):
    return num % 2 == 1

# 测试用例
print("7 是奇数吗？", is_odd(7))  # True
print("8 是奇数吗？", is_odd(8))  # False


# -----------------------------
# 练习 7：计算一个数的阶乘
# -----------------------------
print("练习 7：计算阶乘函数")

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 测试用例
print("5 的阶乘是：", factorial(5))  # 120
print("0 的阶乘是：", factorial(0))  # 1
