from collections import Counter


def job(r_dict, _list, d):
    if d == M:
        print(*_list)
        return

    for k, v in r_dict.items():
        if v:
            r_dict[k] -= 1
            job(r_dict, _list + [k], d + 1)
            r_dict[k] += 1


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
rest_dict = dict(sorted(Counter(num_list).items(), key=lambda x: x[0]))
job(rest_dict, [], 0)
