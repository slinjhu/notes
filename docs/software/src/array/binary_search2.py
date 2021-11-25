def binary_search2(xx, target):
    """
    Binary search with 2 states
    :param xx: an increasing sorted array of integers. Duplicates allowed.
    :param target:
    :return: index of the 1st occurrence if found, otherwise the insertion index
    """
    left, right = -1, len(xx)
    while left + 1 < right:
        mid = (left + right) // 2
        if xx[mid] >= target:
            right = mid
        else:
            left = mid
    return right

