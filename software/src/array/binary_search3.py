def binary_search3(xx, target):
    """
    :param xx: an increasingly sorted array of integers. Duplicates allowed.
    :param target:
    :return: index of ANY occurrence if found, otherwise the insertion index
    """
    u1, u2 = 0, len(xx) - 1
    while u1 <= u2:
        mid = (u1 + u2) // 2
        if xx[mid] == target:
            return mid
        elif xx[mid] < target:
            u1 = mid + 1
        else:
            u2 = mid - 1
    return u1
