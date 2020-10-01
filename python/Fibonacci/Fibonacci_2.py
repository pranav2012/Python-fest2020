# Binet's Formula can be used to calculate F(n) in O(1) time.
# F(n) = (phi^n - psi^n) / sqrt(5),
# where, phi = (1 + sqrt(5))/2, psi = (1 - sqrt(5))/2

# It is mathematically accurate,
# but due to limited precision, it is not practical for larger numbers.

from math import sqrt

phi = (1 + sqrt(5)) / 2
psi = (1 - sqrt(5)) / 2

n = int(input())
ans = (phi**n - psi**n) / sqrt(5)

print("F(%d) = %d" % (n, ans))
