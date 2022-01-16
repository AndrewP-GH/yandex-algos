def is_prime(n):
    if n == 1:
        return True, None
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False, i
        i = i + 1
    return True, None


def eratosthenes(n):
    numbers = list(range(0, n+1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num*num, n+1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    least_prime = [0] * (n+1)
    primes = []
    for i in range(2, n+1):
        if least_prime[i] == 0:
            least_prime[i] = i
            primes.append(i)
        for p in primes:
            x = i * p
            if (x > n) or (p > least_prime[i]):
                break
            least_prime[x] = p
    return primes


if __name__ == '__main__':
    res = get_least_primes_linear(111)
    print('\n'.join(['%s %s' % (i, res[i]) for i in range(len(res))]))

