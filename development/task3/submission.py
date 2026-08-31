import sys


def main() -> None:
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    mod = 998244353
    if 3 * k > n:
        print(0)
        return
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod
    ans = 0
    p = 1
    for i in range(n, 3 * k - 1, -1):
        c = fact[n] * inv_fact[i] % mod * inv_fact[n - i] % mod
        ans = (ans + c * p) % mod
        p = p * 25 % mod
    print(ans)


main()
