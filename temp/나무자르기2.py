n, m = [int(k) for k in input().split()]
length = list(map(int, input().split()))

length.sort(reverse=True)

def find_upper_length(h):
    total_length = 0
    for index, each_length in enumerate(length):
        if each_length < h:
            break
        else:
            total_length += each_length-h
    return total_length

def test_binary(x, y):
    middle = int((x+y)/2)
    if x+1 == y:
        return x
    upper_length = find_upper_length(middle)
    if upper_length > m:
        return test_binary(middle, y)
    elif upper_length == m:
        return middle
    else:
        return test_binary(x, middle)

max_length = length[0]

print(test_binary(0, n))
