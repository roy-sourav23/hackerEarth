# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/anti-plaindrome-2-72ff6f62/

t = int(input())
for _ in range(t):
    s = input()
    ap = lambda s: ''.join(sorted(s))
    print("-1") if s == s[::-1] else print(ap(s))
    
        