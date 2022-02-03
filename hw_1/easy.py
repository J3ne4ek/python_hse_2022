def get_fib(n):
    fibs = [0] * n
    fibs[0] = fibs[1] = 1
    for i in range(2, n):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs