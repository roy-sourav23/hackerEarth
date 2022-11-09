# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

size = input()
arr = input()

def divisibility(arr):
    num = ''.join([x[-1] for x in arr.split()])
    return "Yes" if (int(num) % 10) == 0 else "No"

print(divisibility(arr))
