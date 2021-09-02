# 冒泡算法排序
def bubbleSort(numbers):
    for j in range(1, len(numbers)):
        for i in range(len(numbers) - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                print(numbers)  # 单次变化
    return numbers  # 最后结果


if __name__ == '__main__':
    numbers = [12, 21, 1, 24, 424, 53, 23, 54, 64, 756, 3, 2, 245, 43]
    print(numbers)
    numbers = bubbleSort(numbers)
    print(numbers)
