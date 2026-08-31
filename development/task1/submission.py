import sys


def main() -> None:
    prefix = sys.stdin.readline().strip()
    tail_len = 7
    lo = int(prefix) * 10**tail_len
    hi = lo + 10**tail_len
    limit = int(hi**0.5) + 1
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= limit:
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
        i += 1
    primes = [j for j in range(2, limit + 1) if sieve[j]]
    flags = bytearray([1]) * (hi - lo)
    for q in primes:
        start = q * q
        if start < lo:
            start = ((lo + q - 1) // q) * q
        if start >= hi:
            continue
        flags[start - lo :: q] = bytearray((hi - 1 - start) // q + 1)
    if lo == 0:
        flags[0] = 0
        flags[1] = 0
    total = flags.count(1)
    needle = prefix
    vip = 0
    pos = flags.find(1)
    while pos != -1:
        if needle in str(lo + pos)[4:]:
            vip += 1
        pos = flags.find(1, pos + 1)
    print(total, vip)


if __name__ == "__main__":
    main()
