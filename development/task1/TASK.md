# Task 1. Prime phone numbers

**Type:** Algorithmic · **Points:** 100 · **Time limit:** 1 second · **Memory limit:** 1024 MB

## Statement

MTS has launched a promotion, "Simple means beautiful".

A phone number is 11 digits long; the first 4 digits are the prefix. Under this promotion a subscriber may pick, among the numbers with a given prefix, a number that is a prime.

VIP clients get an extra service: they may pick a number with the given prefix that is, first, a prime and, second, contains the prefix as a substring of the main part of the number (the part that follows the prefix). For example, the number 89169891691 satisfies these properties (for the prefix 8916).

Given a prefix, find the count of numbers available under the promotion and the count of numbers available under the promotion for VIP clients.

## Input

The first line contains a string of 4 digits from 0 to 9 — the given prefix.

## Output

Print two integers — the total count of numbers available under the promotion (including the VIP numbers) and the count of numbers available for VIP clients.

## Example

| Input | Output |
| --- | --- |
| `8916` | `396749 120` |
