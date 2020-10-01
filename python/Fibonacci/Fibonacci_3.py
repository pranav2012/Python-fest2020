# Fibonacci numbers can also be calculated using matrix exponentiation.
# The matrix [F_n F_(n+1)] is equivalent to [F_0 F_1] P^n
# where, P =  0 1
#             1 1
# P^n can be calculated in log n time.

n = int(input())

b = list(bin(n)[2:])

cur = [0, 1, 1, 1]
result = [1, 0, 0, 1] # identity matrix

while b:
    if b.pop() == '1':
        # if the bit is set, then we should multiply the current value with the result
        result = [
            result[0]*cur[0] + result[1]*cur[2],
            result[0]*cur[1] + result[1]*cur[3],
            result[2]*cur[0] + result[3]*cur[2],
            result[2]*cur[1] + result[3]*cur[3]
        ]
    cur = [
        cur[0]*cur[0] + cur[1]*cur[2],
        cur[0]*cur[1] + cur[1]*cur[3],
        cur[2]*cur[0] + cur[3]*cur[2],
        cur[2]*cur[1] + cur[3]*cur[3]
    ]

# result is now equal to P^n, so we can get n'th fibonacci easily now.
ans = result[2]

print("F(%d) = %d" % (n, ans))
