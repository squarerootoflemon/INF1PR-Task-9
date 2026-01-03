n = 0
s = 0

x = int(input())

# loop
while x != -1:

    if n == 0:
        m = x
    else:
        if x < m:
            m = x

    s = s + x
    n = n + 1

    x = int(input())

# after loop
if n == 0:
    m = -1
    a = -1
else:
    a = s / n

# output
print("n =", n)
print("s =", s)
print("m =", m)
print("a =", a)
# figured out how to git :)
