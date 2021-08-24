# while循环
numbers = input("请输入一组数字，以逗号分隔：").split(",")
print(numbers)
x = 0
while x < len(numbers):
    print(numbers[x])
    x += 1
