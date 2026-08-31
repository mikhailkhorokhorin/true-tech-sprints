import sys

MOD = 998244353


def main() -> None:
    n = int(sys.stdin.readline())
    bad = 0
    c = 1
    for j in range(3):
        bad = (bad + c * pow(25, n - j, MOD)) % MOD
        if n - j == 0:
            break
        c = c * (n - j) % MOD * pow(j + 1, MOD - 2, MOD) % MOD
    total = pow(26, n, MOD)
    ans = (1 - bad * pow(total, MOD - 2, MOD)) % MOD
    print(ans % MOD)


main()
