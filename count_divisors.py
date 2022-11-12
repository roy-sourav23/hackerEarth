# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

l, r, k = list(map(int, input().split()))
count = 0
for x in range(l, r+1):
    if x%k == 0:
        count += 1 
print(f"{count}")
