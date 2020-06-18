
def traffic_fee(per_fee, record):
    """

    :param per_fee: 每次乘车的费用
    :param record: 一个月乘车的次数
    :return:
    """
    i = 1
    total_fee = 0
    per_fee1 = per_fee
    while i <= record:
        # if total_fee > 100 and total_fee <= 150:
        #     per_fee = per_fee * 0.8
        # if  total_fee > 150 and total_fee <=300:
        #     per_fee = per_fee * 0.5
        if total_fee < 100:
            per_fee1 = per_fee
        elif total_fee <= 150:
            per_fee1 = per_fee * 0.8
        elif total_fee <= 300:
            per_fee1 = per_fee * 0.5
        else:
            per_fee1 = per_fee
        total_fee = total_fee + per_fee1
        print('第{}天,单日消费{},消费累计{}'.format(i, per_fee1, total_fee))
        i = i + 1
    return total_fee


def main():
    fee = traffic_fee(12, 22)
    print('每个月的车费：{}'.format(fee))


if __name__ == '__main__':

    main()
