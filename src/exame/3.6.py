# 输入个人收入金额，输出需要缴纳的个人所得税，并输出扣税后的实际收入

def rate(income):
    rates = 0
    if 1 < income <= 5000:
        rates = 0
    elif 5000 < income <= 8000:
        rates = 0.03
    elif 8000 < income <= 17000:
        rates = 0.1
    elif 17000 < income <= 30000:
        rates = 0.2
    elif 30000 < income <= 40000:
        rates = 0.25
    elif 40000 < income <= 60000:
        rates = 0.3
    elif 60000 < income <= 85000:
        rates = 0.35
    elif income > 85000:
        rates = 0.45

    print('税前收入为：' + str(income) + '元')
    print('个人所得税率为：' + str(rates))
    print('应缴纳：' + str(income * rates) + '元')
    print('税后实际收入为：', '%.2f' % (income * (1 - rates)), '元')


def main():
    income = float(input('请输入收入金额：'))
    rate(income)


if __name__ == '__main__':
    main()
