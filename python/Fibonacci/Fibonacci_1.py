# The Fibonacci sequence is defined as follows:
# F(0)=0
# F(1)=1
# F(n)=F(n−1)+F(n−2)

# F(n) can be easily calculated in linear time by calculating the terms one by one.

n = int(input())

if n < 2:
    print("F(%d) = %d" % (n, n))

else:
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    print("F(%d) = %d" % (n, b))
