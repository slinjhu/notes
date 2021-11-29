from heapq import heapify, heappop, heappush


def heap_sort(xx):
    min_heap = []
    for x in xx:
        heappush(min_heap, x)
    result = []
    while len(min_heap):
        result.append(heappop(min_heap))
    return result


if __name__ == '__main__':
    xx = [4, 2, 1, 5, 3, 2, 4]
    xx = heap_sort(xx)
    print(xx)