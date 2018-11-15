

# iterative version:
def sum_iterative(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


# recursive version:
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)


# test iterative version of sum
print('Iterative sum: ', sum_iterative(100))
# test recursive version of sum
print('Recursive sum:', sum_recursive(100))
