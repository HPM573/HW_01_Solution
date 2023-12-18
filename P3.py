

def sum_iterative(n):
    """
    This function returns the sum of the first n natural numbers using an iterative approach.
    :param n: (int)
    :return: the sum of the first n natural numbers
    """
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


# recursive version:
def sum_recursive(n):
    """
    This function returns the sum of the first n natural numbers using a recursive approach.
    :param n: (int)
    :return: the sum of the first n natural numbers
    """
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)


# test iterative version of sum
print('Iterative sum: ', sum_iterative(100))
# test recursive version of sum
print('Recursive sum:', sum_recursive(100))
