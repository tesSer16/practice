import heapq
import sys


for _ in range(int(input())):
    activated = [0] * 10**6
    min_heap, max_heap = [], []
    for i in range(int(input())):
        com, num = (sys.stdin.readline().rstrip()).split()
        num = int(num)
        if com == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            activated[i] = 1
        else:
            if num == 1:
                while max_heap and not activated[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    activated[heapq.heappop(max_heap)[1]] = 0
            else:
                while min_heap and not activated[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    activated[heapq.heappop(min_heap)[1]] = 0

        while max_heap and not activated[max_heap[0][1]]:
            heapq.heappop(max_heap)
        while min_heap and not activated[min_heap[0][1]]:
            heapq.heappop(min_heap)

    print("%d %d" % (-max_heap[0][0], min_heap[0][0])) if max_heap and min_heap else print("EMPTY")
