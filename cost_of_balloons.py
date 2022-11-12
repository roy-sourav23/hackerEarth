# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/

t = int(input())
def total_cost(n1, n2, g, p):
    c1, c2 = n1*g + n2*p, n1*p + n2*g
    return min(c1, c2)
for _ in range(t):
    g, p = list(map(int, input().split()))
    n = int(input())
    f = ''
    l = ''
    for _ in range(n):
        a = input()
        f += a[0]
        l += a[-1]
    n1 = f.count("1")
    n2 = l.count("1")
    print(f"{total_cost(n1, n2, g, p)}")
 