# Task 2. Probability of an MTS-string

**Type:** Algorithmic · **Points:** 100 · **Time limit:** 1 second · **Memory limit:** 1024 MB

## Statement

Call a string an MTS-string if all characters but three can be removed from it so that the remaining three letters spell the word MTS.

A string consisting of lowercase Latin letters is built by a uniformly random choice among all strings of length n. What is the probability that this string is an MTS-string?

## Input

The first line contains one integer n — the length of the string (1 ≤ n ≤ 10^5).

## Output

The probability can be uniquely written as a fraction p/q, where p and q are coprime and the denominator is coprime with 998244353. Print the value p·q^(-1) modulo 998244353, that is, the number 0 ≤ x ≤ 998244353 such that q·x has the same remainder modulo 998244353 as p.

## Examples

| Input | Output |
| --- | --- |
| `4` | `448903698` |
| `2` | `0` |
