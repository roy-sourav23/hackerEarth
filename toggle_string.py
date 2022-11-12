# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

s = list(input())
toggle = lambda l : l.lower() if l.isupper() else l.upper()
result = ''.join(list(map(toggle, s)))
print(result)
    
