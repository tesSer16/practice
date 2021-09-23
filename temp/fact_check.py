def factorization(num):
    result_dict = {}
    d = 2

    while d <= num:
        if num % d == 0:
            if d in result_dict:
                result_dict[d] += 1
            else:
                result_dict[d] = 1
            num = num / d
        else:
            d += 1

    return result_dict


def check(num, dic):
    if len(dic) <= 1:
        return False

    str_num = str(num)
    for item in dic.items():
        for i in item:
            if i == 1:
                continue
            str_i = str(i)
            if str_num.startswith(str_i):
                str_num = str_num[len(str_i):]
            else:
                return False

    if str_num:
        return False
    else:
        return True


if __name__ == "__main__":
    n = 1856314
    i = 2
    while True:
        n_dic = factorization(n)
        if check(n, n_dic):
            print(n, n_dic)
        n += 1
        if n >= 10 ** i:
            print("-----%d-----" % (10 ** i))
            i += 1


        
